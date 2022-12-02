# **[inputs] digital-crown**

## The Digital Crown is the primary hardware input for all Apple Watch models.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-digital-crown-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-digital-crown-intro_2x.png)

As people turn the Digital Crown, it generates information you can use to enhance or facilitate interactions with your app, like scrolling or operating standard or custom controls.

**NOTE**Apps don't respond to presses on the Digital Crown because watchOS reserves these interactions for system-provided functionality like revealing the Home Screen.

Apple Watch Series 4 and later provides haptic feedback for the Digital Crown, which gives people a more tactile experience as they scroll through content. By default, the system provides linear haptic *detents* — or taps — as people turn the Digital Crown a specific distance. Some system controls, like table views, provide detents as new items scroll onto the screen.

# **Best practices**

**Provide visual feedback in response to Digital Crown interactions.** For example, pickers change the currently displayed value as people use the Digital Crown. If you track turns directly, use this data to update your interface programmatically. If you don’t provide visual feedback, people are likely to assume that turning the Digital Crown has no effect in your app.

**Update your interface to match the speed with which people turn the Digital Crown.** People expect turning the Digital Crown to give them precise control over an interface, so it works well to use this speed to determine the speed at which you make changes. Avoid updating content at a rate that makes it difficult for people to select values.

**Use the default haptic feedback when it makes sense in your app.** If haptic feedback doesn't feel right in the context of your app — for example, if the default detents don’t match your app’s animation — disable the detents. You can also adjust the haptic feedback behavior for tables, letting them use linear detents instead of row-based detents. For example, if your table has rows with significantly different heights, linear detents may give people a more consistent experience.

# **Platform considerations**

*Not supported in iOS, iPadOS, macOS, or tvOS.*