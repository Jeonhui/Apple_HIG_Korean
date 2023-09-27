# **[inputs] gyro-and-accelerometer**

## On-device gyroscopes and accelerometers can supply data about a device's movement in the physical world.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-gyroscope-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-gyroscope-intro_2x.png)

You can use accelerometer and gyroscope data to enable experiences based on real-time, motion-based information in apps and games that run in iOS, iPadOS, and watchOS. tvOS apps can use gyroscope data from the Siri Remote. For developer guidance, see [Core Motion](https://developer.apple.com/documentation/coremotion).

# **Best practices**

**Use motion data only to offer a tangible benefit to people.** For example, a fitness app might use the data to provide feedback about people’s activity and general health, and a game might use the data to enhance gameplay. Avoid gathering data simply to have the data.

**IMPORTANT**If your experience needs to access motion data from a device, you must provide copy that explains why. The first time your app or game tries to access this type of data, the system includes your copy in a permission request, where people can grant or deny access.

**Outside of active gameplay, avoid using accelerometers or gyroscopes for the direct manipulation of your interface.** Some motion-based gestures may be difficult to replicate precisely, may be physically challenging for some people to perform, and may affect battery usage.

# **Platform considerations**

*No additional considerations for iOS, iPadOS, macOS, tvOS, or watchOS.*