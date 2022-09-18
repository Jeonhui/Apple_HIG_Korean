# **[Platforms] Designing for iOS**

### **People depend on their iPhone to help them stay connected, play games, view media, accomplish tasks, and track personal data in any location and while on the go.**

As you begin designing your app or game for iOS, start by understanding the following fundamental device characteristics and patterns that distinguish the iOS experience. Using these characteristics and patterns to inform your design decisions can help you provide an app or game that iPhone users appreciate.

### **Display.**

iPhone has a medium-sized, high-resolution display.

### **Ergonomics.**

People generally hold their iPhone in one or both hands as they interact with it, switching between landscape and portrait orientations as needed. While people are interacting with the device, their viewing distance tends to be no more than a foot or two.

### **Inputs.**

Multi-Touch [gestures](../inputs/touchscreen-gestures.md),[onscreen keyboards](../components/selection-and-input/onscreen-keyboards.md), and [voice](../technologies/siri/introduction.md) control let people perform actions and accomplish meaningful tasks while they’re on the go. In addition, people often want apps to use their [location](../patterns/accessing-private-data.md) and input from the device’s [accelerometer and gyroscope](../inputs/gyro-and-accelerometer.md), and they may also want to participate in [spatial interactions](../inputs/spatial-interactions.md).

### **App interactions.**

Sometimes, people spend just a minute or two checking on event or social media updates, tracking data, or sending messages. At other times, people can spend an hour or more browsing the web, playing games, or enjoying media. People typically have multiple apps open at the same time, and they appreciate switching frequently among them.

### **System features.**

iOS provides several features that help people interact with the system and their apps in familiar, consistent ways.

- [Widgets](../components/system-experiences/widgets.md)
- [Home Screen quick actions](../components/system-experiences/home-screen-quick-actions.md)
- [Spotlight](../patterns/searching.md)
- [Shortcuts](../technologies/siri/shortcuts-and-suggestions.md)
- [Activity views](../components/menus-and-actions/activity-views.md)


## **Best practices**

Great iPhone experiences integrate the platform and device capabilities that people value most. To help your design feel at home in iOS, prioritize the following ways to incorporate these features and capabilities.

- Help people focus on primary tasks and content by limiting the number of onscreen controls while making secondary details and actions discoverable with minimal interaction.
- Adapt seamlessly to appearance changes — like device orientation, Dark Mode, and Dynamic Type — letting people choose the configurations that work best for them.
- Enable interactions that support the way people usually hold their device. For example, it tends to be easier and more comfortable for people to reach a control when it’s located in the middle or bottom area of the display, so it’s especially important let people swipe to navigate back or initiate actions in a list row.
- With people’s permission, integrate information available through platform capabilities in ways that enhance the experience without asking people to enter data. For example, you might accept payments, provide security through biometric authentication, or offer features that use the device’s location.