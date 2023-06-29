Gauges
======

A gauge displays a specific numerical value within a range of values.![A stylized representation of a circular numeric gauge above a linear percentage gauge. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/f32c347212ea5d73bc63f86d1a866225/components-gauges-intro@2x.png)

In addition to indicating the current value in a range, a gauge can provide more context about the range itself. For example, a temperature gauge can use text to identify the highest and lowest temperatures in the range and display a spectrum of colors that visually reinforce the changing values.

[Anatomy](/design/human-interface-guidelines/gauges#Anatomy)
------------------------------------------------------------

A gauge uses a circular or linear path to represent a range of values, mapping the current value to a specific point on the path. A standard gauge displays an indicator that shows the current value’s location; a gauge that uses the capacity style displays a fill that stops at the value’s location on the path.

Circular and linear gauges in both standard and capacity styles are also available in a variant that’s visually similar to watchOS complications. This variant — called accessory — works well in iOS Lock Screen widgets and anywhere you want to echo the appearance of complications.

Note

In addition to gauges, macOS also supports level indicators, some of which have visual styles that are similar to gauges. For guidance, see [macOS](/design/human-interface-guidelines/gauges#macOS)
.

[Best practices](/design/human-interface-guidelines/gauges#Best-practices)
--------------------------------------------------------------------------

**Write succinct labels that describe the current value and both endpoints of the range.** Although not every gauge style displays all labels, VoiceOver reads the visible labels to help people understand the gauge without seeing the screen.

**Consider filling the path with a gradient to help communicate the purpose of the gauge.** For example, a temperature gauge might use colors that range from red to blue to represent temperatures that range from hot to cold.

[Platform considerations](/design/human-interface-guidelines/gauges#Platform-considerations)
--------------------------------------------------------------------------------------------

*No additional considerations for iOS, iPadOS, visionOS, or watchOS. Not supported in tvOS.*

### [macOS](/design/human-interface-guidelines/gauges#macOS)

In addition to supporting gauges, macOS also defines a level indicator that displays a specific numerical value within a range. You can configure a level indicator to convey capacity, rating, or — rarely — relevance.

The capacity style can depict discrete or continuous values.

![An image of a continuous capacity indicator that uses the default green fill to indicate an amount of about two-thirds of the total capacity.](https://docs-assets.developer.apple.com/published/8d1f4b040b7736a1ba832b93a7dc3bfb/indicators-continuous@2x.png)

**Continuous.** A horizontal translucent track that fills with a solid bar to indicate the current value.

![An image of a discrete capacity indicator that uses the default green fill to indicate an amount of three-quarters of the total capacity.](https://docs-assets.developer.apple.com/published/f148e7934177391449aa61cc97ffea49/indicators-discrete@2x.png)

**Discrete.** A horizontal row of separate, equally sized, rectangular segments. The number of segments matches the total capacity, and the segments fill completely — never partially — with color to indicate the current value.

**Consider using the continuous style for large ranges.** A large value range can make the segments of a discrete capacity indicator too small to be useful.

**Consider changing the fill color to inform people about significant parts of the range.** By default, the fill color for both capacity indicator styles is green. If it makes sense in your app, you can change the fill color when the current value reaches certain levels, such as very low, very high, or just past the middle. You can change the fill color of the entire indicator or you can use the tiered state to show a sequence of several colors in one indicator, as shown below.

![An image of a continuous capacity indicator in which the leftmost one-eigth is red, the next three-eighths are yellow, the next one-fourth is green, and the last one-fourth is unfilled.](https://docs-assets.developer.apple.com/published/6d84b116ed12ffcabc2a36fb8f63e31e/indicators-continuous-tiered@2x.png)Tiered level appearanceFor guidance using the rating style to help people rank something, see [Rating indicators](/design/human-interface-guidelines/rating-indicators)
.

Although rarely used, the relevance style can communicate relevancy using a shaded horizontal bar. For example, a relevance indicator might appear in a list of search results, helping people visualize the relevancy of the results when sorting or comparing multiple items.

[Resources](/design/human-interface-guidelines/gauges#Resources)
----------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/gauges#Related)

[Ratings and reviews](/design/human-interface-guidelines/ratings-and-reviews)


#### [Developer documentation](/design/human-interface-guidelines/gauges#Developer-documentation)

[`Gauge`](/documentation/SwiftUI/Gauge)


[`NSLevelIndicator`](/documentation/appkit/nslevelindicator)


[Change log](/design/human-interface-guidelines/gauges#Change-log)
------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| September 23, 2022 | New page. |

