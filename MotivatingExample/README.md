# Motivating Example

This folder contains the motivating example of the paper.

![motivatingExample](simulinkModel.png "Motivating Example")

## Folder and Files

The main folder contains:

- `start/` contains the start configuration:
  - `scc_v0.rt`: the contract of the _Cruise Controller_
  - `we_v0.rt`: the contract of the _Weather Controller_
  - `composition.rt`: the contract of the _Composition_ between _Cruise Controller_ and _Weather Controller_
  - `refinement.rt`: the contracts for both the _Controller_ and the _Composition_
- `controller.rt`: the contract of the _Controller_ that the composition of _Cruise Controller_ and _Weather Controller_ must always respect
- `OTA-scc/` contains an OTA that attempts to update the _Cruise Controller_ contract from _SCC_v0_ to _SCC_v1_
- `OTA-we/` contains an OTA that attempts to update the _Weather Controller_ contract from _WE_v0_ to _WE_v1_
- `OTA-sccwe/` contains an OTA that attempts to update both the _Cruise Controller_ (_SCC_v0_) and _Weather Controller_ (_WE_v1_) contracts. Since we are updating two components, we first run their composition, and then check whether the _Composition_ refines the _Controller_ contract.

Each subfolder contains a `run.sh` script to execute the checks.

## Configuration

Place the required JAR file in this folder before running the tests.

## Run

```terminal
./run.sh
```

## Results of the OTAs

- **OTA-scc**: The new _Cruise Controller_ contract (_SCC_v1_) **refines** the original configuration (_SCC_v0_). ✅ **OTA-scc compatible update**.
- **OTA-we**: The new _Weather Controller_ contract (_WE_v1_) **does not** refine the original configuration (_WE_v0_). ❌ **OTA-we not recommended**.
- **OTA-sccwe**: The _Composition_ of the new _Cruise Controller_ (_SCC_v1_) and _Weather Controller_ (_WE_v1_) contracts **refines** the _Controller_ contract. ✅ **_OTA-sccwe_ compatible update**.
