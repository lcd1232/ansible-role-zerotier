# Molecule Test for ansible-role-zerotier

This directory contains molecule tests for the ansible-role-zerotier Ansible role.

## Test Scenarios

### default

The default test scenario verifies that the role correctly handles `ansible_facts['local']` access.

#### What it tests:
- Ensures that `ansible_facts['local']['zerotier']['node_id']` can be properly accessed
- Verifies the fix for the issue where `ansible_local` was incorrectly mixed with `ansible_facts['local']`
- Tests the role's ability to work with custom facts

#### Running the tests:

To run the test playbook directly:
```bash
ansible-playbook molecule/default/test-playbook.yml
```

To run the full molecule test suite (requires Docker):
```bash
molecule test
```

To run only the converge step:
```bash
molecule converge
```

## Test Files

- `molecule.yml` - Molecule configuration
- `converge.yml` - Main playbook that applies the role
- `verify.yml` - Verification tests
- `test-playbook.yml` - Standalone test playbook that can be run without Docker
- `create.yml` - Creates test instances (Docker containers)
- `destroy.yml` - Destroys test instances

## Requirements

- molecule
- molecule-docker (for Docker driver)
- ansible
- docker (for running full molecule tests)

Install with:
```bash
pip install molecule molecule-docker
```
