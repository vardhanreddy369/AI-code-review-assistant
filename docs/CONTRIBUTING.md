# Contributing Guide

## Welcome!

We welcome contributions to the AI Code Review Assistant project. This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Focus on the code, not the person
- Help others learn and grow
- Report issues through proper channels

## Getting Started

1. **Fork** the repository
2. **Clone** your fork locally
3. **Create** a new branch for your feature
4. **Make** your changes
5. **Write** tests for new functionality
6. **Submit** a pull request

## Development Setup

```bash
# Clone repository
git clone https://github.com/yourusername/AI-code-review-assistant.git
cd AI-code-review-assistant

# Setup development environment
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Setup pre-commit hooks
pre-commit install
```

## Branch Naming

Use descriptive branch names:
- `feature/add-new-analysis-type`
- `fix/webhook-validation-bug`
- `docs/update-setup-guide`
- `refactor/optimize-ml-inference`

## Commit Messages

Follow conventional commits:

```
type(scope): subject

body

footer
```

**Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

**Examples:**
```
feat(ml): add support for new code patterns
fix(api): resolve webhook signature validation
docs(setup): update installation instructions
```

## Pull Request Process

1. **Update** documentation and tests
2. **Run** tests locally: `pytest tests/`
3. **Check** code style: `flake8 .`
4. **Create** descriptive PR title and description
5. **Link** related issues: `Fixes #123`
6. **Wait** for code review and CI checks

### PR Checklist

- [ ] Tests pass locally
- [ ] Code follows style guide
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
- [ ] Commit history is clean

## Code Style

### Python

```bash
# Format code
black .

# Check style
flake8 .
pylint app/

# Type checking
mypy app/
```

### TypeScript/React

```bash
# Format code
npm run format

# Check linting
npm run lint

# Type checking
npm run type-check
```

### Standards

- **Python**: PEP 8
- **TypeScript**: ESLint config
- **Comments**: Clear, meaningful comments
- **Functions**: Small, focused functions
- **Types**: Use type hints (Python) and TypeScript

## Testing

### Backend Tests

```bash
cd backend

# Run all tests
pytest

# Run specific test
pytest tests/test_analysis.py

# With coverage
pytest --cov=app --cov-report=html
```

### ML Service Tests

```bash
cd ml-service

pytest tests/
```

### Dashboard Tests

```bash
cd dashboard

npm test
npm run build
```

## Documentation

- Update `README.md` for major changes
- Add docstrings to new functions
- Document API changes
- Update `docs/` as needed

### DocString Format

```python
"""
Short description.

Long description if needed.

Args:
    param1: Description
    param2: Description

Returns:
    Description of return value

Raises:
    ExceptionType: When this happens
"""
```

## Report Issues

### Security Issues

**Do not** open public issues for security vulnerabilities. Email: security@example.com

### Bug Reports

Include:
- Python/Node version
- Reproduction steps
- Expected vs actual behavior
- Error messages/logs
- Screenshots if applicable

### Feature Requests

- Clear description of use case
- Proposed implementation approach
- Why this feature is needed
- Similar projects for reference

## Development Tips

### Debugging

```python
# Python debugging
import pdb; pdb.set_trace()

# Or use debugger
breakpoint()
```

```typescript
// TypeScript/React debugging
debugger;  // Browser DevTools
console.log();
```

### Local Testing with Webhook

```bash
# Use ngrok to expose local server
ngrok http 8000

# Configure webhook URL with ngrok URL
```

### Database Management

```bash
# Create new migration
alembic revision --autogenerate -m "description"

# Apply migration
alembic upgrade head

# Rollback
alembic downgrade -1
```

## Review Process

1. **Initial Review**: Linting, formatting, tests
2. **Code Review**: Logic, design, best practices
3. **Approval**: At least one maintainer approval
4. **Merge**: Maintainer merges after CI passes

## Releasing

For maintainers:

```bash
# Update version
bumpversion patch  # or minor/major

# Tag release
git tag v1.0.0
git push origin v1.0.0

# Create release notes
# Build and publish
```

## Learning Resources

- [Project Documentation](./docs/)
- [API Reference](./docs/API.md)
- [Architecture](./docs/ARCHITECTURE.md)
- [Setup Guide](./docs/SETUP.md)

## Questions?

- Open an issue with `[question]` tag
- Join our discussions
- Check existing issues and documentation

## Recognition

Contributors will be recognized:
- In CONTRIBUTORS.md
- In release notes
- Special badges for major contributions

---

**Thank you for contributing!** ❤️
