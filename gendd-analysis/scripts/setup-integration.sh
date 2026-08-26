#!/bin/bash

# GenDD-Flow Integration Setup Script
# This script helps integrate GenDD-Flow with a target repository

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GENDDFLOW_ROOT="$(dirname "$SCRIPT_DIR")"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_header() {
    echo -e "\n${BLUE}========================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}========================================${NC}\n"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

show_help() {
    cat << EOF
GenDD-Flow Integration Setup

Usage: ./setup-integration.sh [OPTIONS] <target-repository-path>

Options:
  -h, --help          Show this help message
  -l, --link          Create symbolic link to GenDD-Flow in target repo
  -c, --cursorrules   Copy .cursorrules template to target repo
  -b, --bridge        Create bridge .cursorrules file in target repo
  -a, --all           Do all of the above
  -w, --workspace     Create a Cursor workspace file

Examples:
  ./setup-integration.sh -l /path/to/my-project
  ./setup-integration.sh --all /path/to/my-project
  ./setup-integration.sh -w /path/to/my-project

EOF
}

create_symlink() {
    local target_path="$1"
    local link_path="$target_path/.genddflow"
    
    if [ -L "$link_path" ]; then
        print_warning "Symbolic link already exists at $link_path"
        return 0
    fi
    
    if [ -e "$link_path" ]; then
        print_error "A file or directory already exists at $link_path"
        return 1
    fi
    
    ln -s "$GENDDFLOW_ROOT" "$link_path"
    print_success "Created symbolic link: $link_path → $GENDDFLOW_ROOT"
    
    # Add to .gitignore if not already there
    if [ -f "$target_path/.gitignore" ]; then
        if ! grep -q "^\.genddflow$" "$target_path/.gitignore"; then
            echo ".genddflow" >> "$target_path/.gitignore"
            print_success "Added .genddflow to .gitignore"
        fi
    else
        echo ".genddflow" > "$target_path/.gitignore"
        print_success "Created .gitignore with .genddflow"
    fi
}

create_bridge_cursorrules() {
    local target_path="$1"
    local target_name="$(basename "$target_path")"
    local rules_file="$target_path/.cursorrules"
    
    if [ -f "$rules_file" ]; then
        print_warning ".cursorrules already exists. Creating .cursorrules.genddflow instead"
        rules_file="$target_path/.cursorrules.genddflow"
    fi
    
    cat > "$rules_file" << EOF
# Cursor Rules for $target_name

## GenDD-Flow Integration

This repository uses GenDD-Flow workflows for AI-assisted development.

**GenDD-Flow Location**: .genddflow/ (or $GENDDFLOW_ROOT)

### Quick Reference

When working on this repository, reference GenDD-Flow workflows:

| Task | Command |
|------|---------|
| Enhance requirements | Read @.genddflow/workflows/enhance-acceptance-criteria.md |
| Identify test gaps | Read @.genddflow/workflows/identify-test-gaps.md |
| Generate unit tests | Read @.genddflow/workflows/generate-unit-tests.md |
| Create context pack | Read @.genddflow/workflows/create-context-pack.md |
| Generate C4 diagrams | Read @.genddflow/workflows/generate-architecture-diagrams.md |
| Brownfield analysis | Read @.genddflow/workflows/brownfield-repository-analysis.md |

### The Five Frameworks

1. **Story Quality (Shift-Left)**: Use AI to enhance acceptance criteria before development
2. **Test Gap Identification**: Map what tests should exist vs what does exist
3. **Context Packs**: Create lightweight Markdown files for AI context
4. **C4 Architecture Diagrams**: Generate system, container, and component views
5. **Brownfield Analysis**: Understand legacy/undocumented systems with 4-pass approach

---

## Repository-Specific Context

### About This Repository
[TODO: Add description of what this repository does]

### Tech Stack
[TODO: List technologies used]
- Language: 
- Framework: 
- Database: 
- Other: 

### Key Integrations
[TODO: List external systems this integrates with]
- 

### Testing
[TODO: Document testing approach]
- Unit Test Framework: 
- Integration Test Framework: 
- E2E Framework: 

### Multi-Tenant
[TODO: Is this multi-tenant? If so, always filter by tenant]
- Multi-tenant: Yes/No
- Tenant ID field: 

### Compliance
[TODO: List compliance requirements]
- 

---

## Before Generating Code

1. Check if similar code exists in this repository
2. Reference the appropriate GenDD-Flow workflow
3. Follow existing patterns in this codebase
4. Include error handling
5. Consider security and compliance requirements
6. Add appropriate tests
EOF

    print_success "Created bridge .cursorrules at $rules_file"
    print_warning "TODO: Edit $rules_file to add repository-specific context"
}

create_workspace() {
    local target_path="$1"
    local target_name="$(basename "$target_path")"
    local workspace_file="$target_path/${target_name}-with-genddflow.code-workspace"
    
    cat > "$workspace_file" << EOF
{
    "folders": [
        {
            "name": "$target_name",
            "path": "."
        },
        {
            "name": "GenDD-Flow",
            "path": "$GENDDFLOW_ROOT"
        }
    ],
    "settings": {
        "files.associations": {
            "*.md": "markdown"
        }
    }
}
EOF

    print_success "Created Cursor workspace file: $workspace_file"
    echo -e "  Open with: ${BLUE}cursor \"$workspace_file\"${NC}"
}

# Parse arguments
LINK=false
CURSORRULES=false
BRIDGE=false
WORKSPACE=false
TARGET_PATH=""

while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            show_help
            exit 0
            ;;
        -l|--link)
            LINK=true
            shift
            ;;
        -c|--cursorrules)
            CURSORRULES=true
            shift
            ;;
        -b|--bridge)
            BRIDGE=true
            shift
            ;;
        -w|--workspace)
            WORKSPACE=true
            shift
            ;;
        -a|--all)
            LINK=true
            BRIDGE=true
            WORKSPACE=true
            shift
            ;;
        *)
            if [ -z "$TARGET_PATH" ]; then
                TARGET_PATH="$1"
            else
                print_error "Unknown argument: $1"
                show_help
                exit 1
            fi
            shift
            ;;
    esac
done

# Validate target path
if [ -z "$TARGET_PATH" ]; then
    print_error "Target repository path is required"
    show_help
    exit 1
fi

# Resolve to absolute path
TARGET_PATH="$(cd "$TARGET_PATH" 2>/dev/null && pwd)" || {
    print_error "Target path does not exist: $TARGET_PATH"
    exit 1
}

print_header "GenDD-Flow Integration Setup"
echo "GenDD-Flow Path: $GENDDFLOW_ROOT"
echo "Target Repository: $TARGET_PATH"

# If no specific actions selected, show interactive menu
if [ "$LINK" = false ] && [ "$CURSORRULES" = false ] && [ "$BRIDGE" = false ] && [ "$WORKSPACE" = false ]; then
    echo ""
    echo "Select integration options:"
    echo "  1) Create symbolic link (.genddflow)"
    echo "  2) Create bridge .cursorrules file"
    echo "  3) Create Cursor workspace file"
    echo "  4) All of the above"
    echo "  5) Cancel"
    echo ""
    read -p "Enter choice [1-5]: " choice
    
    case $choice in
        1) LINK=true ;;
        2) BRIDGE=true ;;
        3) WORKSPACE=true ;;
        4) LINK=true; BRIDGE=true; WORKSPACE=true ;;
        5) echo "Cancelled."; exit 0 ;;
        *) print_error "Invalid choice"; exit 1 ;;
    esac
fi

# Execute selected actions
print_header "Setting Up Integration"

if [ "$LINK" = true ]; then
    create_symlink "$TARGET_PATH"
fi

if [ "$BRIDGE" = true ]; then
    create_bridge_cursorrules "$TARGET_PATH"
fi

if [ "$WORKSPACE" = true ]; then
    create_workspace "$TARGET_PATH"
fi

print_header "Integration Complete!"

echo "Next steps:"
echo "  1. Open the target repository in Cursor"
if [ "$WORKSPACE" = true ]; then
    echo "     Or open the workspace file: cursor \"$TARGET_PATH/$(basename "$TARGET_PATH")-with-genddflow.code-workspace\""
fi
if [ "$BRIDGE" = true ]; then
    echo "  2. Edit .cursorrules to add repository-specific context"
fi
echo "  3. Start using GenDD-Flow workflows!"
echo ""
echo "Example prompt in Cursor:"
echo "  \"Read @.genddflow/workflows/identify-test-gaps.md and analyze this repository for test gaps\""

