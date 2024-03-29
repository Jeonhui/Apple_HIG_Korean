Charts
======

Organize data in a chart to communicate information with clarity and visual appeal.![A stylized representation of a bar chart. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/e60ec631128010abf4cf09793552a20a/components-charts-intro@2x.png)

An effective chart highlights a few key pieces of information in a dataset, helping people gain insights and make decisions. For example, people might use a chart to:

* Learn how upcoming weather conditions might affect their plans.
* Analyze stock prices to understand past performance and discover trends.
* Review fitness data to monitor their progress and set new goals.

To learn about designing charts to enhance your experience, see [Charting data](/design/human-interface-guidelines/charting-data)
; for developer guidance, see [Creating a chart using Swift Charts](/documentation/Charts/Creating-a-chart-using-Swift-Charts)
.

[Anatomy](/design/human-interface-guidelines/charts#Anatomy)
------------------------------------------------------------

A chart comprises several graphical elements that depict the values in a dataset and convey information about them.

![A bar chart with callouts that identify chart components, such as axes, grid lines, marks, ticks, axis value labels, and the overall plot area.](https://docs-assets.developer.apple.com/published/99ff482fad4dd4768a7280ce055bbe5d/charts-anatomy@2x.png)

A *mark* is a visual representation of a data value. You create a chart by supplying one or more series of data values, assigning each value to a mark. To specify the style of chart you want to display — such as bar chart, line chart, or scatter plot — you choose a mark type, such as bar, line, or point (for guidance, see [Marks](/design/human-interface-guidelines/charts#Marks)
). The general task of depicting individual data values in a chart is called *plotting*, and the area that contains the marks is called the *plot area*.

To depict a value, each type of mark uses visual attributes that are determined by a scale, which maps data values like numbers, dates, or categories to visual characteristics like position, color, or height. For example, a bar mark can use a particular height to represent the magnitude of a value and a particular position to represent the time at which the value occurred.

To give people the context they need to interpret a chart’s visual characteristics, you supply descriptive content that can take a few different forms.

You can use an *axis* to help define a frame of reference for the data represented by a set of marks. Many charts display a pair of axes at the edges of the plot area — one horizontal and one vertical — where each axis represents a variable like time, amount, or category.

An axis can include *ticks*, which are reference points that help people visually locate the position of important values along the axis, such as a 0, 50%, and 100%. Many charts display *grid lines* that each extend from a tick across the plot area to help people visually estimate a data value when its mark isn’t near an axis.

You also have multiple ways to describe chart elements to help people interpret the data and to highlight the key information you want to communicate. For example, you can supply *labels* that name items like axes, grid lines, ticks, or marks, and *accessibility labels* that describe chart elements for people who use assistive technologies. To provide context and additional details, you can create descriptive titles, subtitles, and annotations. When needed, you can also create a legend, which describes chart properties that aren’t related to a mark’s position, such as the use of color or shape to denote different value categories.

Clear, accurate descriptions can help make a chart more approachable and accessible; to learn about additional ways to improve the accessibility of your chart, see [Enhancing the accessibility of a chart](/design/human-interface-guidelines/charts#Enhancing-the-accessibility-of-a-chart)
.

[Marks](/design/human-interface-guidelines/charts#Marks)
--------------------------------------------------------

**Choose a mark type based on the information you want to communicate about the data.** Some of the most familiar mark types are bar, line, and point; for developer guidance on these and other mark types, see [Swift Charts](/documentation/Charts)
.

*Bar* marks work well in charts that help people compare values in different categories or view the relative proportions of various parts in a whole. When used to help people understand data that changes over time, bar charts work especially well when each value can represent a sum, like the total number of steps taken in a day.

![A bar chart that depicts the number of steps for each day in a month.](https://docs-assets.developer.apple.com/published/2c2b96ba943f42c1d5d1f9a32e3734eb/bar-marks@2x.png)

*Line* marks can also show how values change over time. In a line chart, a line connects all data values in one series of data. The slope of the line reveals the magnitude of change between data values and can help people visualize overall trends.

![A line chart that depicts the performance of a stock over a five-year period.](https://docs-assets.developer.apple.com/published/ae570f541a660059884424b2f29c9fab/line-marks@2x.png)

*Point* marks help you depict individual data values as visually distinct marks. A set of point marks can show how two different properties of your data relate to each other, helping people inspect individual data values and identify outliers and clusters.

![A point-mark chart that depicts per-day readings of heartbeats per minute over a 5 1/2-month period.](https://docs-assets.developer.apple.com/published/8ba49655d7d3feae136d58e18b54edf3/point-marks@2x.png)

**Consider combining mark types when it adds clarity to your chart.** For example, if you use a line chart to show a change over time, you might want to add point marks on top of the line to highlight individual data points. By combining points with a line, you can help people understand the overall trend while also drawing their attention to individual values.

[Axes](/design/human-interface-guidelines/charts#Axes)
------------------------------------------------------

**Use a fixed or dynamic axis range depending on the meaning of your chart.** In a *fixed* range, the upper and lower bounds of the axis never change, whereas in a *dynamic* range, the upper and lower bounds can vary with the current data. Consider using a fixed range when specific minimum and maximum values are meaningful for all possible data values. For example, people expect a chart that shows a battery’s current charge to have a minimum value of 0% (completely empty) and a maximum value of 100% (completely full).

![A partial screenshot of Battery Settings on iPhone, which uses a chart to depict battery charge over time, where the charge can vary within a fixed range from 0% to 100%.](https://docs-assets.developer.apple.com/published/6b8fbf83fbad897aaaa55967ec3f66b3/fixed-range-axis@2x.png)In contrast, consider using a dynamic range when the possible data values can vary widely and you want the marks to fill the available plot area. For example, the upper bound of the Y axis range in the Health app’s Steps chart varies so that the largest number of steps in a particular time period is close to the top of the chart.

![A screenshot of the Steps chart in the Health app on iPhone, which shows the total number of steps for a single day.](https://docs-assets.developer.apple.com/published/be7b88a567c6e793dd58a510fb42b5f4/dynamic-range-axis-small@2x.png)![A screenshot of the Steps chart in the Health app on iPhone, which shows the average number of steps per day in a one-month period.](https://docs-assets.developer.apple.com/published/c7019380e638f896bd3f5632f5ae7e79/dynamic-range-axis-large@2x.png)**Define the value of the lower bound based on mark type and chart usage.** For example, bar charts can work well when you use zero for the lower bound of the Y axis, because doing so lets people visually compare the relative heights of individual bars to get a reasonable estimate of their values. In contrast, defining a lower bound of zero can sometimes make meaningful differences between values more difficult to discern. For example, a heart rate chart that always uses zero for the lower bound could obscure important differences between resting and active readings because the differences occur in a range that’s far from zero.

**Prefer familiar sequences of values in the tick and grid-line labels for an axis.** For example, if you use a common number sequence like 0, 5, 10, etc., people are likely to know at a glance that each tick value equals the previous value plus five. Even though a sequence like 1, 6, 11, etc., follows the same rule, it’s not common, so most people are likely to spend extra time thinking about the interval between values.

**Tailor the appearance of grid lines and labels to a chart’s use cases.** Too many grid lines can be visually overwhelming, distracting people from the data; too few grid lines can make it difficult to estimate a mark’s value. To help you determine the appropriate density and visual weight of these elements, consider a chart’s context in the interface, the interactions you support, and the tasks people can do in the chart. For example, if people can inspect individual data points by interacting with a chart, you might use fewer grid lines and light label colors to ensure the data remains visually prominent.

[Descriptive content](/design/human-interface-guidelines/charts#Descriptive-content)
------------------------------------------------------------------------------------

**Write descriptions that help people understand what a chart does before they view it.** When you provide information-rich titles and labels that describe the purpose and functionality of a chart, you give people the context they need before they dive in and examine the details. Providing context in this way is especially important for VoiceOver users and those with certain types of cognitive disabilities because they rely on your descriptions to understand the purpose and primary message of your chart before they decide to investigate it further.

**Summarize the main message of your chart to help make it approachable and useful for everyone.** Although a primary reason to use a chart is to display the data that supports the main message, it’s essential to summarize key information so that people can grasp it quickly. For example, Weather provides a title and subtitle that succinctly describe the expected precipitation for the next hour, giving people the most important information without requiring them to examine the details of the chart.

![A partial screenshot of the Weather app on iPhone, which uses succinct, plain language to describe the precipitation forecasted for the next 60 minutes.](https://docs-assets.developer.apple.com/published/7ab15e42df1a3dbfffa6427773fa26cc/descriptive-content@2x.png)[Best practices](/design/human-interface-guidelines/charts#Best-practices)
--------------------------------------------------------------------------

**Establish a consistent visual hierarchy that helps communicate the relative importance of various chart elements.** Typically, you want the data itself to be most prominent, while letting the descriptions and axes provide additional context without competing with the data.

**In a compact environment, maximize the width of the plot area to give people enough space to comfortably examine a chart.** To help important data fit well in a given width, ensure that labels on a vertical axis are as short as possible without losing clarity. You might also consider describing units in other areas of the chart, such as in a title, and placing a longer axis label, such as a category name, inside the plot area when doing so doesn’t obscure important information.

**Make every chart in your app accessible.** Charts — like all infographics — need to be fully accessible to everyone, regardless of how they perceive content. For example, it’s essential to support VoiceOver, which describes onscreen content to help people get information and navigate without needing to see the screen (to learn more about VoiceOver, see [Vision](https://www.apple.com/accessibility/vision/)
). In addition to supplying accessibility labels that describe the components of your chart, you can enhance the VoiceOver experience by also using Audio Graphs. [Audio graphs](/documentation/accessibility/audio_graphs)
 provides chart information to VoiceOver, which constructs a set of tones that audibly represent a chart’s data values and their trend; it also lets you present high-level text summaries that provide additional context. For guidance, see [Enhancing the accessibility of a chart](/design/human-interface-guidelines/charts#Enhancing-the-accessibility-of-a-chart)
.

**Let people interact with the data when it makes sense, but don’t require interaction to reveal critical information.** In Stocks, for example, people are often most interested in a stock’s performance over time, so the app displays a line graph that depicts performance during the time period people choose, such as one day, three months, or five years. If people want to explore additional details, they can drag a vertical indicator through the line graph, revealing the value at the selected time.

**Make it easy for everyone to interact with a chart.** Sometimes, chart marks are too small to target with a finger or a pointer, making your chart hard to use for people with reduced motor control and uncomfortable for everyone. When this is the case, consider expanding the hit target to include the entire plot area, letting people scrub across the area to reveal various values.

**Make an interactive chart easy to navigate when using keyboard commands (including full keyboard access) or Switch Control.** By default, these input types tend to visit individual onscreen elements in a linear sequence, such as the sequence of values in a data file. If you want to provide a custom navigation experience in your chart, here are two main ways to do so. The first way is to use accessibility APIs (such as [`accessibilityRespondsToUserInteraction(_:)`](/documentation/SwiftUI/View/accessibilityRespondsToUserInteraction(_:))
) to specify a logical and predictable path through your chart’s information. For example, you might want to let people navigate along the X axis instead of jumping back and forth. The second way — which is particularly useful if you need to present a very large dataset — is to let people move focus among subsets of values instead of navigating through all individual data points. Note that both of these customizations can also enhance the VoiceOver experience, even when your chart isn’t interactive. For guidance, see [Navigation](/design/human-interface-guidelines/accessibility#Navigation)
.

**Help people notice important changes in a chart.** For example, if people don’t notice when marks or axes change, they can misread a chart. Animating such changes can help people notice them, but you need to highlight the changes in other ways, too, to ensure that VoiceOver users and people who turn off animations know about them. For developer guidance, see [`UIAccessibility.Notification`](/documentation/uikit/uiaccessibility/notification)
 (UIKit) or [`NSAccessibility.Notification`](/documentation/appkit/nsaccessibility/notification)
 (AppKit).

**Align a chart with surrounding interface elements.** For example, it often works well to align the leading edge of a chart with the leading edge of other views in a screen. One way to maintain a clean leading edge in a chart is to display the label for each vertical grid line on its trailing side. You might also consider shifting the Y axis to the trailing side of the chart so that its tick labels don’t protrude past the chart’s leading edge. If you end up with a label that doesn’t appear to be associated with anything, you can use a tick to anchor it to a grid line.

[Color](/design/human-interface-guidelines/charts#Color)
--------------------------------------------------------

As in all other parts of your interface, using color in a chart can help you clarify information, evoke your brand, and provide visual continuity. For general guidance on using color in ways that everyone can appreciate, see [Inclusive color](/design/human-interface-guidelines/color#Inclusive-color)
.

**Avoid relying solely on color to differentiate between different pieces of data or communicate essential information in a chart.** Using meaningful color in a chart works well to highlight differences and elevate key details, but it’s crucial to include alternative ways to convey this information so that people can use your chart regardless of whether they can discern colors. One way to supplement color is to use different shapes or patterns to depict different parts of data. For example, in addition to using red and black colors, Health uses two different shapes in the point marks that represent the two components of blood pressure.

![A partial screenshot of the Health app on iPhone showing a blood pressure chart that uses a red circle to represent systolic values and a black diamond to represent diastolic values.](https://docs-assets.developer.apple.com/published/756ade4516fa5fafcffbb1c49c77a462/chart-colors@2x.png)**Aid comprehension by adding visual separation between contiguous areas of color.** For example, in a bar chart that stacks marks in a single row or column, it’s common to assign a different color to each mark. In this design, adding separators between the marks can help people distinguish individual ones.

![A partial screenshot of iPhone Storage Settings, which uses a single bar mark containing several segments of different colors to show the relative space taken by items such as media, apps, and photos. The bar includes a narrow strip of empty space between each pair of segments.](https://docs-assets.developer.apple.com/published/869d72f5ebc394c25ce50d364a4bca6c/chart-colors-stacked@2x.png)[Enhancing the accessibility of a chart](/design/human-interface-guidelines/charts#Enhancing-the-accessibility-of-a-chart)
--------------------------------------------------------------------------------------------------------------------------

When you use Swift Charts to create a chart, you get a default implementation of [Audio graphs](/documentation/accessibility/audio_graphs)
, in addition to a default accessibility element for each mark (or group of marks) that describes its value.

**Consider using Audio Graphs to give VoiceOver users more information about your chart.** You can customize the default Audio Graphs implementation that Swift Charts provides by supplying a chart title and descriptive summary that VoiceOver speaks to help people understand the purpose and main features of your chart. If you don’t use Audio Graphs, you need to provide an overview of the chart’s structure and purpose. For example, you need to identify the chart’s type — such as bar or line — explain what each axis represents, and describe details like the upper and lower axis bounds.

Important

Unlike an image — which requires one descriptive accessibility label — a chart often needs to offer an accessibility label for each important or interactive element. Depending on the purpose of your chart and the scope and density of its marks, you need to decide whether it’s essential to describe each mark or whether it improves the accessibility experience to describe groups of marks. In some cases, it can make sense to use a single accessibility label that provides a succinct, high-level description of the chart, such as when you use a small version of a chart in a button that reveals a more detailed version.

**Write accessibility labels that support the purpose of your chart.** For example, Maps shows elevation changes for a cycling route using a set of individual bars that each represent the elevation for a small portion of the route. The purpose of the chart is to give people a sense of the terrain for the entire route, not to provide individual elevations. For this reason, Maps provides accessibility labels that summarize the elevation changes in a group of bars; it doesn’t provide an accessibility label per bar. In contrast, Health offers an accessibility label for each bar in the Steps chart, because the purpose of the chart is to give people their actual step count for each tracking period.

![A partial screenshot of a bar chart in Maps that shows the range of elevations over the total distance of the trip. A VoiceOver focus indicator is visible on top of the chart, containing approximately one-fifth of the total number of elevation values.](https://docs-assets.developer.apple.com/published/88ef51d10f2f3c6d1afce56176a3c050/bar-chart-with-voiceover-focus@2x.png)For the focused section of this cycling elevation chart, VoiceOver provides the description “From 0.4 miles to 0.7 miles: Climb 70 feet.”The following guidelines can help you write useful accessibility labels for chart elements.

* **Prioritize clarity and comprehensiveness.** In general, it’s rarely enough to merely report a data value unless you also include context that helps people understand it, like the date or location that’s associated with it. Aim to concisely describe the context for a value without repeating information that people can get in other ways, like an axis name that Audio Graphs or your overview provides. Follow context-setting information with a succinct description of the element’s details.
* **Avoid using subjective terms.** Subjective words — like rapidly, gradually, and almost — communicate your interpretation of the data. To help people form their own interpretations, use actual values in your descriptions.
* **Maximize clarity in data descriptions by avoiding potentially ambiguous formats and abbreviations.** For example, using “June 6” is clearer than using “6/6”; similarly, spelling out “60 minutes” or “60 meters” is clearer than using the abbreviation “60m.”
* **Focus on describing what the chart’s details represent, not on what they look like.** Consider a chart that uses red and blue colors to help people visually distinguish two different data series. It’s crucial to create accessibility labels that identify what each series represents, but describing the colors that visually represent them can add unnecessary information and be distracting.
* **Be consistent throughout your app when referring to a specific axis.** For example, if you always mention the X axis first, people can spend less time figuring out which axis is relevant in a description.

**Hide visible text labels for axes and ticks from assistive technologies.** Axis and tick labels help people visually assess trends in a chart and estimate mark values. VoiceOver users can get mark values and trend information through accessibility labels and Audio Graphs, so they don’t generally need the content in the visible labels.

[Platform considerations](/design/human-interface-guidelines/charts#Platform-considerations)
--------------------------------------------------------------------------------------------

*No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS.*

### [watchOS](/design/human-interface-guidelines/charts#watchOS)

**In general, avoid requiring complex chart interactions in your watchOS app.** As much as possible, prefer displaying focused, useful information people can get at a glance and supporting simple interactions when they add value. If you also offer a version of your app in another platform, consider using it to display more details and to support additional interactions with your chart. For example, Heart Rate in watchOS displays a chart of the wearer’s heart-rate data for the current day, whereas the Health app on iPhone displays heart-rate data for several different periods of time and lets people examine individual marks.

[Resources](/design/human-interface-guidelines/charts#Resources)
----------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/charts#Related)

[Charting data](/design/human-interface-guidelines/charting-data)


#### [Developer documentation](/design/human-interface-guidelines/charts#Developer-documentation)

[Swift Charts](/documentation/Charts)


#### [Videos](/design/human-interface-guidelines/charts#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/124/FA764D2D-4E15-4E91-91BA-BDAC80FB901B/6694_wide_250x141_1x.jpg) Design app experiences with charts](https://developer.apple.com/videos/play/wwdc2022/110342) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/124/4BBCB61E-65ED-43FE-8F7B-81524E0C96BE/6692_wide_250x141_1x.jpg) Design an effective chart](https://developer.apple.com/videos/play/wwdc2022/110340) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/124/5D24326E-AAF9-4EDB-8CE1-C12DBFB28F51/6633_wide_250x141_1x.jpg) Hello Swift Charts](https://developer.apple.com/videos/play/wwdc2022/10136) 
[Change log](/design/human-interface-guidelines/charts#Change-log)
------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| September 23, 2022 | New page. |

