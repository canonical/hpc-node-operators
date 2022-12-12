# HPC Node Operators

This repo provides two charms:
* [hpc-node](node/README.md) (for general use)
* [hpc-node-subordinate](subordinate/README.md) (example for demonstration)

See http://github.com/canonical/hpc-cluster.

## To Build

Prerequisites:
* snap
* charmcraft (snap package)
* juju (snap package)

Clone this repository:

```
git clone <repourl>
```

Build (may need to run each `charmcraft` twice):

```
cd hpc-node-operators
for name in node subordinate; do
    (cd ${name}; charmcraft -v pack)
done
```
