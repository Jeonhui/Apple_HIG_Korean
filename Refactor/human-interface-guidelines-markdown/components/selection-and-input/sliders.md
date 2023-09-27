June 21, 2023

 Updated to include guidance for visionOS. Sliders
=======

A slider is a horizontal track with a control, called a thumb, that people can adjust between a minimum and maximum value.![A stylized representation of a brightness slider. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/af60d798eddd3d1594c11faad30df20a/components-slider-intro@2x.png)

As a slider’s value changes, the portion of track between the minimum value and the thumb fills with color. A slider can optionally display left and right icons that illustrate the meaning of the minimum and maximum values.

[Best practices](/design/human-interface-guidelines/sliders#Best-practices)
---------------------------------------------------------------------------

**Customize a slider’s appearance if it adds value.** You can adjust a slider’s appearance — including track color, thumb image and tint color, and left and right icons — to blend with your app’s design and communicate intent. A slider that adjusts image size, for example, could show a small image icon on the left and a large image icon on the right.

**Use familiar slider directions.** People expect the minimum and maximum sides of sliders to be consistent in all apps, with minimum values on the leading side and maximum values on the trailing side (for horizontal sliders) and minimum values at the bottom and maximum values at the top (for vertical sliders). For example, people expect to be able to move a horizontal slider that represents a percentage from 0 percent on the leading side to 100 percent on the trailing side.

**Consider supplementing a slider with a corresponding text field and stepper.** Especially when a slider represents a wide range of values, people may appreciate seeing the exact slider value and having the ability to enter a specific value in a text field. Adding a stepper provides a convenient way for people to increment in whole values. For related guidance, see [Text fields](/design/human-interface-guidelines/text-fields)
 and [Steppers](/design/human-interface-guidelines/steppers)
.

![A partial screenshot of a horizontal linear slider without tick marks, followed by a text field and a stepper. The thumb is in the center of the slider and the text field displays 50%.](https://docs-assets.developer.apple.com/published/7b81536dca93efcad895b4967d8c4031/sliders-text-field@2x.png)

[Platform considerations](/design/human-interface-guidelines/sliders#Platform-considerations)
---------------------------------------------------------------------------------------------

*Not supported in tvOS.*

### [iOS, iPadOS](/design/human-interface-guidelines/sliders#iOS-iPadOS)

**Don’t use a slider to adjust audio volume.** If you need to provide volume control in your app, use a volume view, which is customizable and includes a volume-level slider and a control for changing the active audio output device. For guidance, see [Playing audio](/design/human-interface-guidelines/playing-audio)
.

### [macOS](/design/human-interface-guidelines/sliders#macOS)

Sliders in macOS can also include tick marks, making it easier for people to pinpoint a specific value within the range.

In a linear slider without tick marks, the thumb is round, and the portion of track between the minimum value and the thumb is filled with color. In a linear slider with tick marks, the thumb is directional — pointing toward the tick marks — and the track isn’t tinted. A linear slider often includes supplementary icons that illustrate the meaning of the minimum and maximum values.

In a circular slider, the thumb appears as a small circle. Tick marks, when present, appear as evenly spaced dots around the circumference of the slider.

![A partial screenshot of a horizontal slider with the circular thumb in the middle.](https://docs-assets.developer.apple.com/published/65b348fd67b2f68951a8baba7a92f616/sliders-no-tick-marks@2x.png)Linear slider without tick marks![A partial screenshot of a horizontal slider with the narrow lozenge-shape thumb between two tick marks in the middle of the slider.](https://docs-assets.developer.apple.com/published/d3518d708f370868b90e917f751b9577/sliders-tick-marks@2x.png)Linear slider with tick marks![A partial screenshot of a circular slider with the thumb at the 12 o'clock position.](https://docs-assets.developer.apple.com/published/3f253ed199e7e92b6124e6161dd79152/sliders-circular@2x.png)Circular slider**Consider giving live feedback as the value of a slider changes.** Live feedback shows people results in real time. For example, your Dock icons are dynamically scaled when adjusting the Size slider in Dock settings.

**Choose a slider style that matches peoples’ expectations.** A horizontal slider is ideal when moving between a fixed starting and ending point. For example, a graphics app might offer a horizontal slider for setting the opacity level of an object between 0 and 100 percent. Use circular sliders when values repeat or continue indefinitely. For example, a graphics app might use a circular slider to adjust the rotation of an object between 0 and 360 degrees. An animation app might use a circular slider to adjust how many times an object spins when animated — four complete rotations equals four spins, or 1440 degrees of rotation.

**Consider using a label to introduce a slider.** Labels generally use [sentence-style capitalization](https://help.apple.com/applestyleguide/#/apsgb744e4a3?sub=apdca93e113f1d64)
 and end with a colon. For guidance, see [Labels](/design/human-interface-guidelines/labels)
.

**Use tick marks to increase clarity and accuracy.** Tick marks help people understand the scale of measurements and make it easier to locate specific values.

![A partial screenshot of the Energy Saver settings pane in macOS, cropped to show the slider that controls how long the display remains on after inactivity.](https://docs-assets.developer.apple.com/published/ea283c6d5a597b731b1c6fbacffe73d2/sliders-labels@2x.png)

**Consider adding labels to tick marks for even greater clarity.** Labels can be numbers or words, depending on the slider’s values. It’s unnecessary to label every tick mark unless doing so is needed to reduce confusion. In many cases, labeling only the minimum and maximum values is sufficient. When the values of the slider are nonlinear, like in the Energy Saver settings pane, periodic labels provide context. It’s also a good idea to provide a [help tag](https://developer.apple.com/design/human-interface-guidelines/offering-help)
 that displays the value of the thumb when people hold their pointer over it.

### [visionOS](/design/human-interface-guidelines/sliders#visionOS)

**Prefer horizontal sliders.** It’s generally easier for people to gesture from side to side than up and down.

### [watchOS](/design/human-interface-guidelines/sliders#watchOS)

A slider is a horizontal track — appearing as a set of discrete steps or as a continuous bar — that represents a finite range of values. People can tap buttons on the sides of the slider to increase or decrease its value by a predefined amount.

![An illustration that represents a watchOS screen with a brightness slider.](https://docs-assets.developer.apple.com/published/9b2bead664b38a208db844c2f30b4ed2/sliders-watchos@2x.png)

**If necessary, create custom glyphs to communicate what the slider does.** The system displays plus and minus signs by default.

[Resources](/design/human-interface-guidelines/sliders#Resources)
-----------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/sliders#Related)

[Steppers](/design/human-interface-guidelines/steppers)


[Pickers](/design/human-interface-guidelines/pickers)


#### [Developer documentation](/design/human-interface-guidelines/sliders#Developer-documentation)

[`Slider`](/documentation/SwiftUI/Slider)


[`UISlider`](/documentation/uikit/uislider)


[`NSSlider`](/documentation/appkit/nsslider)


[`WKInterfaceSlider`](/documentation/watchkit/wkinterfaceslider)


[Change log](/design/human-interface-guidelines/sliders#Change-log)
-------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 21, 2023 | Updated to include guidance for visionOS. |

