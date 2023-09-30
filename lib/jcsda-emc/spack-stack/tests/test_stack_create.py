import os

import pytest

import spack
import spack.main

stack_create = spack.main.SpackCommand("stack")


# Find spack-stack directory assuming this Spack instance
# is a submodule of spack-stack.
def stack_path(*paths):
    stack_dir = os.path.dirname(spack.paths.spack_root)

    if not os.path.exists(os.path.join(stack_dir, ".spackstack")):
        return None

    return os.path.join(stack_dir, *paths)


test_dir = stack_path("envs", "unit-tests", "stack-create")


def all_templates():
    template_path = stack_path("configs", "templates")
    if template_path:
        _, templates, _ = next(os.walk(template_path))
        return list(templates)
    else:
        return None


def all_sites():
    site_path = stack_path("configs", "sites")
    if site_path:
        _, sites, _ = next(os.walk(site_path))
        return list(sites)
    else:
        return None


def all_containers():
    container_path = stack_path("configs", "containers")
    if container_path:
        _, _, containers = next(os.walk(container_path))
        # Exclude files like "README.md"
        containers = [x for x in containers if x.endswith(".yaml")]
        return containers
    else:
        return None


@pytest.mark.extension("stack")
@pytest.mark.parametrize("template", all_templates())
@pytest.mark.filterwarnings("ignore::UserWarning")
def test_apps(template):
    if not template:
        return
    stack_create("create", "env", "--template", template, "--dir", test_dir, "--overwrite")


@pytest.mark.extension("stack")
@pytest.mark.parametrize("site", all_sites())
@pytest.mark.filterwarnings("ignore::UserWarning")
def test_sites(site):
    if not site:
        return
    stack_create("create", "env", "--site", site, "--dir", test_dir, "--overwrite")


@pytest.mark.extension("stack")
@pytest.mark.parametrize("container", all_containers())
@pytest.mark.filterwarnings("ignore::UserWarning")
def test_containers(container):
    if not container:
        return
    container_wo_ext = os.path.splitext(container)[0]
    stack_create("create", "ctr", container_wo_ext, "--dir", test_dir, "--overwrite")

@pytest.mark.extension("stack")
@pytest.mark.filterwarnings("ignore::UserWarning")
def test_modulesys():
    modsystems = {"lmod", "tcl"}
    for modulesys in modsystems:
        stack_create("create", "env", "--site", "hera", "--dir", test_dir, "--overwrite", "--modulesys", modulesys)
    modules_yaml_path = os.path.join(test_dir, "common", "modules.yaml")
    with open(modules_yaml_path, "r") as f:
        modules_yaml_txt = f.read()
    assert "%s:" % modulesys in modules_yaml_txt
    assert "%s:" % list(modsystems.difference(modulesys))[0] not in modules_yaml_txt

@pytest.mark.extension("stack")
@pytest.mark.filterwarnings("ignore::UserWarning")
def test_upstream():
    stack_create("create", "env", "--site", "hera", "--dir", test_dir, "--overwrite", "--upstream", "/test/path/to/upstream/env")
    spack_yaml_path = os.path.join(test_dir, "spack.yaml")
    with open(spack_yaml_path, "r") as f:
        spack_yaml_txt = f.read()
    assert "install_tree: /test/path/to/upstream/env" in spack_yaml_txt
