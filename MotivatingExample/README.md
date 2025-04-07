# Motivating Example

This folder contains the motivating example of the paper.

## Folder

Each folder has two contracts:

- `cc.rt` the contract of the Cruise Controller
- `ve.rt` the contract of the Vehicle

First, we run the composition, obtaining `composition.rt`.
Then, we run the refinement, checking if `composition.rt` refines `controlled_vehicle.rt`.

- `first` contains the first configuration
- `second` contains the second configuration, after updating both the vehicle and the cruise controller component contracts.
- `controlled_vehicle.rt` is the contract that the composition must always respect.

## Configuration

You need to save the JAR file in this folder before running the tests

## Run

```terminal
./motivating.sh
```

The script run the composition and then the refinement for both the configurations (`first` and `second`).
In particular, `second` configuration is an OTA on both vehicle and cruise controller of the `first` configuration.
