Steppers
========

A stepper is a two-segment control that people use to increase or decrease an incremental value.![A stylized representation of a stepper control. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/091580d0530042f6685cd17226140173/components-stepper-intro@2x.png)

A stepper sits next to a field that displays its current value, because the stepper itself doesn’t display a value.

[Best practices](/design/human-interface-guidelines/steppers#Best-practices)
----------------------------------------------------------------------------

**Make the value that a stepper affects obvious.** A stepper itself doesn’t display any values, so make sure people know which value they’re changing when they use a stepper.

**Consider pairing a stepper with a text field when large value changes are likely.** Steppers work well by themselves for making small changes that require a few taps or clicks. By contrast, people appreciate the option to use a field to enter specific values, especially when the values they use can vary widely. On a printing screen, for example, it can help to have both a stepper and a text field to set the number of copies.

[Platform considerations](/design/human-interface-guidelines/steppers#Platform-considerations)
----------------------------------------------------------------------------------------------

*No additional considerations for iOS, iPadOS, or visionOS. Not supported in watchOS or tvOS.*

### [macOS](/design/human-interface-guidelines/steppers#macOS)

**For large value ranges, consider supporting Shift-click to change the value quickly.** If your app benefits from larger changes in a stepper’s value, it can be useful to let people Shift-click the stepper to change the value by more than the default increment (by 10 times the default, for example).

[Resources](/design/human-interface-guidelines/steppers#Resources)
------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/steppers#Related)

[Pickers](/design/human-interface-guidelines/pickers)


[Text fields](/design/human-interface-guidelines/text-fields)


#### [Developer documentation](/design/human-interface-guidelines/steppers#Developer-documentation)

[`UIStepper`](/documentation/uikit/uistepper)


[`NSStepper`](/documentation/appkit/nsstepper)


