# maze_with_car-model

## Clone the Repository

First, clone the repository that contains the model and necessary files. If you haven't already cloned it, use the following command:

```bash
git clone https://github.com/zaynabahmad/maze_with_car-model.git
cd maze_with_car-model
```

# Running the Model in Gazebo

Follow the steps below to launch your model in Gazebo:

1. **Set the Platform Environment Variable**
   Ensure you set the `QT_QPA_PLATFORM` to `wayland` to configure the appropriate platform for the display.

   Run the following command:

   ```bash
   export QT_QPA_PLATFORM=wayland
   ```
2. **Launch Ignition Gazebo**
   Start Gazebo by specifying your model's `.sdf` file. This will load the environment and display the simulation.

   Run the following command:

   ```bash
   ign gazebo maze/model.sdf
   ```
