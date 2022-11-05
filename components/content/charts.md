# **[components] charts**
## A chart helps you communicate data in a graphical, approachable way.
> 차트는 접근 가능한 그래픽 방식으로 데이터를 전달하는 데 도움이 됩니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images//intro/components/charts-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images//intro/components/charts-intro-dark_2x.png)

An effective chart highlights a few key pieces of information in a dataset, helping people gain insights and make decisions. For example, people might use a chart to:
> 효과적인 차트는 데이터 세트의 몇 가지 핵심 정보를 강조하여 사람들이 통찰력을 얻고 의사 결정을 내리는 데 도움을 줍니다. 예를 들어, 사용자는 차트를 사용하여 다음을 수행할 수 있습니다.
>




- Learn how upcoming weather conditions might affect their plans
- >  앞으로의 기상 조건이 계획에 어떤 영향을 미치는지 알아봅니다.

- Analyze stock prices to understand past performance and discover trends
- >  주가 분석을 통해 과거 실적 파악 및 동향 파악

- Review fitness data to monitor their progress and set new goals
- >  피트니스 데이터를 검토하여 진행 상황을 모니터링하고 새로운 목표를 설정합니다.


To learn about designing charts to enhance your experience, see [Charting data](../patterns/charting-data); for developer guidance, see [Creating a chart using Swift Charts](https://developer.apple.com/documentation/charts/creating-a-chart-using-swift-charts).
> 사용자 환경을 개선하기 위한 차트 설계에 대한 자세한 내용은 데이터 차트를 참조하십시오. 개발자 지침은 스위프트 차트를 사용하여 차트 만들기를 참조하십시오.
>




# **Anatomy**

A chart comprises several graphical elements that depict the values in a dataset and convey information about them.
> 차트는 데이터 세트의 값을 묘사하고 그에 대한 정보를 전달하는 몇 가지 그래픽 요소로 구성된다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/content/charts/images/charts-anatomy_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/content/charts/images/charts-anatomy_2x.png)

A *mark* is a visual representation of a data value. You create a chart by supplying one or more series of data values, assigning each value to a mark. To specify the style of chart you want to display — such as bar chart, line chart, or scatter plot — you choose a mark type, such as bar, line, or point (for guidance, see [Marks](https://developer.apple.com/design/human-interface-guidelines/components/content/charts#marks)). The general task of depicting individual data values in a chart is called *plotting*, and the area that contains the marks is called the *plot area*.
> 마크는 데이터 값을 시각적으로 표현한 것입니다. 하나 이상의 데이터 값을 제공하고 각 값을 표시에 할당하여 차트를 만듭니다. 막대 차트, 꺽은선형 차트 또는 산점도와 같이 표시할 차트 스타일을 지정하려면 막대, 선 또는 점과 같은 표시 유형을 선택합니다(자세한 내용은 표시 참조). 차트에서 개별 데이터 값을 나타내는 일반적인 작업을 플롯이라고 하며, 마크가 들어 있는 영역을 플롯 영역이라고 합니다.
>




To depict a value, each type of mark uses visual attributes that are determined by a scale, which maps data values like numbers, dates, or categories to visual characteristics like position, color, or height. For example, a bar mark can use a particular height to represent the magnitude of a value and a particular position to represent the time at which the value occurred.
> 값을 묘사하기 위해 각 유형의 표시는 숫자, 날짜 또는 범주와 같은 데이터 값을 위치, 색상 또는 높이와 같은 시각적 특성에 매핑하는 척도에 의해 결정되는 시각적 속성을 사용합니다. 예를 들어, 바 표시는 값의 크기를 나타내기 위해 특정 높이를 사용하고 값이 발생한 시간을 나타내기 위해 특정 위치를 사용할 수 있습니다.
>




To give people the context they need to interpret a chart’s visual characteristics, you supply descriptive content that can take a few different forms.
> 차트의 시각적 특성을 해석하는 데 필요한 컨텍스트를 사람들에게 제공하기 위해 몇 가지 다른 형태를 취할 수 있는 설명 콘텐츠를 제공합니다.
>




You can use an *axis* to help define a frame of reference for the data represented by a set of marks. Many charts display a pair of axes at the edges of the plot area — one horizontal and one vertical — where each axis represents a variable like time, amount, or category.
> 축을 사용하면 일련의 표시로 표현되는 데이터에 대한 참조 프레임을 쉽게 정의할 수 있습니다. 많은 차트는 플롯 영역의 가장자리에 한 쌍의 축(수평과 수직)을 표시합니다. 여기서 각 축은 시간, 양 또는 범주와 같은 변수를 나타냅니다.
>




An axis can include *ticks*, which are reference points that help people visually locate the position of important values along the axis, such as a 0, 50%, and 100%. Many charts display *grid lines* that each extend from a tick across the plot area to help people visually estimate a data value when its mark isn’t near an axis.
> 축에는 0, 50%, 100%와 같은 축을 따라 중요한 값의 위치를 시각적으로 찾는 데 도움이 되는 기준점인 눈금이 포함될 수 있습니다. 많은 차트는 눈금에서 그림 영역을 가로질러 각각 연장된 격자선을 표시하여 데이터 표시가 축 근처에 없을 때 데이터 값을 시각적으로 추정하는 데 도움이 됩니다.
>




You also have multiple ways to describe chart elements to help people interpret the data and to highlight the key information you want to communicate. For example, you can supply *labels* that name items like axes, grid lines, ticks, or marks, and *accessibility labels* that describe chart elements for people who use assistive technologies. To provide context and additional details, you can create descriptive titles, subtitles, and annotations. When needed, you can also create a legend, which describes chart properties that aren’t related to a mark’s position, such as the use of color or shape to denote different value categories.
> 또한 여러 가지 방법으로 차트 요소를 설명하여 사람들이 데이터를 해석하는 데 도움을 주고 전달할 주요 정보를 강조 표시할 수 있습니다. 예를 들어 축, 격자선, 눈금 또는 표시와 같은 항목의 이름을 지정하는 레이블과 보조 기술을 사용하는 사람들을 위한 차트 요소를 설명하는 내게 필요한 옵션 레이블을 제공할 수 있습니다. 상황별 및 추가 세부 정보를 제공하기 위해 설명 제목, 부제 및 주석을 작성할 수 있습니다. 필요한 경우 범례를 만들 수도 있습니다. 범례는 다른 값 범주를 나타내기 위해 색상이나 모양을 사용하는 등 표시 위치와 관련이 없는 차트 속성을 설명합니다.
>




Clear, accurate descriptions can help make a chart more approachable and accessible; to learn about additional ways to improve the accessibility of your chart, see [Enhancing the accessibility of a chart](https://developer.apple.com/design/human-interface-guidelines/components/content/charts#enhancing-the-accessibility-of-a-chart).
> 명확하고 정확한 설명을 통해 차트를 보다 쉽게 접근하고 액세스할 수 있습니다. 차트의 접근성을 향상시키는 추가 방법에 대한 자세한 내용은 차트 접근성 향상을 참조하십시오.
>




# **Marks**

**Choose a mark type based on the information you want to communicate about the data.** Some of the most familiar mark types are bar, line, and point; for developer guidance on these and other mark types, see [Swift Charts](https://developer.apple.com/documentation/charts).
> 데이터에 대해 전달할 정보를 기반으로 마크 유형을 선택합니다. 가장 익숙한 마크 유형으로는 막대, 선 및 점이 있습니다. 이러한 마크 유형과 기타 마크 유형에 대한 개발자 지침은 스위프트 차트를 참조하십시오.
>




*Bar* marks work well in charts that help people compare values in different categories or view the relative proportions of various parts in a whole. When used to help people understand data that changes over time, bar charts work especially well when each value can represent a sum, like the total number of steps taken in a day.
> 막대 표시는 사람들이 서로 다른 범주의 값을 비교하거나 전체적으로 다양한 부품의 상대적 비율을 보는 데 도움이 되는 차트에서 잘 작동합니다. 막대형 차트는 사람들이 시간에 따라 변하는 데이터를 이해하는 데 도움을 주는 데 사용되며, 특히 하루 동안 수행된 총 단계 수와 같이 각 값이 합을 나타낼 수 있을 때 잘 작동합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/content/charts/images/bar-marks_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/content/charts/images/bar-marks_2x.png)

*Line* marks can also show how values change over time. In a line chart, a line connects all data values in one series of data. The slope of the line reveals the magnitude of change between data values and can help people visualize overall trends.
> 선 표시는 시간이 지남에 따라 값이 어떻게 변하는지 보여줄 수도 있습니다. 꺽은선형 차트에서 선은 하나의 데이터 시리즈에 있는 모든 데이터 값을 연결합니다. 선의 기울기는 데이터 값 사이의 변화의 크기를 나타내며 사람들이 전반적인 추세를 시각화하는 데 도움이 될 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/content/charts/images/line-marks_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/content/charts/images/line-marks_2x.png)

*Point* marks help you depict individual data values as visually distinct marks. A set of point marks can show how two different properties of your data relate to each other, helping people inspect individual data values and identify outliers and clusters.
> 점 표시는 개별 데이터 값을 시각적으로 구별되는 표시로 표현하는 데 도움이 됩니다. 점 표시 집합은 데이터의 서로 다른 두 속성이 서로 어떻게 관련되어 있는지 보여 주며, 사람들이 개별 데이터 값을 검사하고 특이치와 군집을 식별하는 데 도움이 됩니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/content/charts/images/point-marks_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/content/charts/images/point-marks_2x.png)

**Consider combining mark types when it adds clarity to your chart.** For example, if you use a line chart to show a change over time, you might want to add point marks on top of the line to highlight individual data points. By combining points with a line, you can help people understand the overall trend while also drawing their attention to individual values.
> 차트에 명확성을 추가할 때는 마크 유형을 조합하는 것이 좋습니다. 예를 들어, 선형 차트를 사용하여 시간에 따른 변화를 표시하는 경우, 라인 위에 점 표시를 추가하여 개별 데이터 점을 강조할 수 있습니다. 점을 선과 결합하면 사람들이 전반적인 추세를 이해하는 데 도움이 될 수 있으며 개별적인 가치에도 주의를 기울일 수 있습니다.
>




# **Axes**

**Use a fixed or dynamic axis range depending on the meaning of your chart.** In a *fixed* range, the upper and lower bounds of the axis never change, whereas in a *dynamic* range, the upper and lower bounds can vary with the current data. Consider using a fixed range when specific minimum and maximum values are meaningful for all possible data values. For example, people expect a chart that shows a battery’s current charge to have a minimum value of 0% (completely empty) and a maximum value of 100% (completely full).
> 차트의 의미에 따라 고정 또는 동적 축 범위를 사용합니다. 고정 범위에서는 축의 상한과 하한이 변경되지 않지만 동적 범위에서는 현재 데이터에 따라 상한과 하한이 달라질 수 있습니다. 가능한 모든 데이터 값에 대해 특정 최소값과 최대값이 유의한 경우 고정 범위를 사용하는 것이 좋습니다. 예를 들어, 사람들은 배터리의 현재 충전량을 나타내는 차트의 최소값이 0%(완전 비어 있음)이고 최대값이 100%(완전 가득 차 있음)라고 예상합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/content/charts/images/fixed-range-axis_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/content/charts/images/fixed-range-axis_2x.png)

In contrast, consider using a dynamic range when the possible data values can vary widely and you want the marks to fill the available plot area. For example, the upper bound of the Y axis range in the Health app’s Steps chart varies so that the largest number of steps in a particular time period is close to the top of the chart.
> 반대로 가능한 데이터 값이 크게 달라질 수 있고 사용 가능한 플롯 영역을 채우려는 경우 동적 범위를 사용하는 것을 고려해 보십시오. 예를 들어 Health 앱의 Steps 차트에서 Y축 범위의 상한은 특정 기간 동안 가장 많은 수의 스텝이 차트 상단에 근접하도록 변경됩니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/content/charts/images/dynamic-range-axis-large_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/content/charts/images/dynamic-range-axis-large_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/components/content/charts/images/bar-marks_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/content/charts/images/bar-marks_2x.png)

**Define the value of the lower bound based on mark type and chart usage.** For example, bar charts can work well when you use zero for the lower bound of the Y axis, because doing so lets people visually compare the relative heights of individual bars to get a reasonable estimate of their values. In contrast, defining a lower bound of zero can sometimes make meaningful differences between values more difficult to discern. For example, a heart rate chart that always uses zero for the lower bound could obscure important differences between resting and active readings because the differences occur in a range that’s far from zero.
> 표시 유형 및 차트 사용량에 따라 하한 값을 정의합니다. 예를 들어 막대형 차트는 Y 축의 하한에 0을 사용할 때 잘 작동합니다. 이렇게 하면 사람들이 개별 막대의 상대적인 높이를 시각적으로 비교하여 값을 합리적으로 추정할 수 있기 때문입니다. 반대로, 0의 하한을 정의하면 값 사이의 의미 있는 차이를 식별하기가 더 어려워질 수 있습니다. 예를 들어, 하한에 항상 0을 사용하는 심박수 차트는 0에서 멀리 떨어진 범위에서 발생하기 때문에 휴식과 활성 판독치 사이의 중요한 차이를 모호하게 할 수 있습니다.
>




**Prefer familiar sequences of values in the tick and grid-line labels for an axis.** For example, if you use a common number sequence like 0, 5, 10, etc., people are likely to know at a glance that each tick value equals the previous value plus five. Even though a sequence like 1, 6, 11, etc., follows the same rule, it’s not common, so most people are likely to spend extra time thinking about the interval between values.
> 축에 대한 눈금 및 격자선 레이블의 익숙한 값 시퀀스를 선호합니다. 예를 들어 0, 5, 10 등과 같은 공통 숫자 시퀀스를 사용하면 사람들은 각 눈금 값이 이전 값과 5를 더한 값과 같다는 것을 한 눈에 알 수 있습니다. 1, 6, 11 등과 같은 순서가 같은 규칙을 따르더라도, 그것은 흔하지 않기 때문에 대부분의 사람들은 값 사이의 간격을 생각하는데 여분의 시간을 소비할 가능성이 있다.
>




**Tailor the appearance of grid lines and labels to a chart’s use cases.**Too many grid lines can be visually overwhelming, distracting people from the data; too few grid lines can make it difficult to estimate a mark’s value. To help you determine the appropriate density and visual weight of these elements, consider a chart’s context in the interface, the interactions you support, and the tasks the chart enables. For example, if people can inspect individual data points by interacting with a chart, you might use fewer grid lines and light label colors to ensure the data remains visually prominent.
> 그리드 선과 레이블의 모양을 차트의 사용 사례에 맞게 조정합니다.격자선이 너무 많으면 시각적으로 압도되어 데이터로부터 사람들의 주의를 분산시킬 수 있으며 격자선이 너무 적으면 표시 값을 추정하기 어려울 수 있다. 이러한 요소의 적절한 밀도와 시각적 가중치를 결정하는 데 도움이 되도록 인터페이스의 차트 컨텍스트, 지원하는 상호 작용 및 차트에서 사용할 수 있는 작업을 고려하십시오. 예를 들어, 사람들이 차트와 상호 작용하여 개별 데이터 점을 검사할 수 있는 경우 데이터를 시각적으로 두드러지게 유지하기 위해 더 적은 격자선과 밝은 레이블 색상을 사용할 수 있습니다.
>




# **Descriptive content**

**Write descriptions that help people understand what a chart does before they view it.** When you provide information-rich titles and labels that describe the purpose and functionality of a chart, you give people the context they need before they dive in and examine the details. Providing context in this way is especially important for VoiceOver users and those with certain types of cognitive disabilities because they rely on your descriptions to understand the purpose and primary message of your chart before they decide to investigate it further.
> 차트를 보기 전에 차트를 이해하는 데 도움이 되는 설명을 작성합니다. 차트의 목적과 기능을 설명하는 정보가 풍부한 제목과 레이블을 제공하는 경우, 사용자가 세부 정보를 살펴보고 들어가기 전에 필요한 컨텍스트를 제공합니다. 이러한 방식으로 컨텍스트를 제공하는 것은 VoiceOver 사용자와 특정 유형의 인지 장애가 있는 사람들에게 특히 중요합니다. 왜냐하면 그들은 차트를 더 조사하기로 결정하기 전에 차트의 목적과 주요 메시지를 이해하기 위해 당신의 설명에 의존하기 때문입니다.
>




**Summarize the main message of your chart to help make it approachable and useful for everyone.** Although a primary reason to use a chart is to display the data that supports the main message, it’s essential to summarize key information so that people can grasp it quickly. For example, Weather provides a title and subtitle that succinctly describe the expected precipitation for the next hour, giving people the most important information without requiring them to examine the details of the chart.
> 차트를 사용하는 주된 이유는 주요 메시지를 지원하는 데이터를 표시하기 위한 것이지만 주요 정보를 빠르게 파악할 수 있도록 요약하는 것이 중요합니다. 예를 들어, Weather는 다음 한 시간 동안의 예상 강수량을 간결하게 설명하는 제목과 부제를 제공하여 사람들에게 차트의 세부 사항을 조사할 필요 없이 가장 중요한 정보를 제공합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/content/charts/images/descriptive-content_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/content/charts/images/descriptive-content_2x.png)

# **Best practices**

**Establish a consistent visual hierarchy that helps communicate the relative importance of various chart elements.** Typically, you want the data itself to be most prominent, while letting the descriptions and axes provide additional context without competing with the data.
> 다양한 차트 요소의 상대적 중요도를 전달하는 데 도움이 되는 일관된 시각적 계층을 설정합니다. 일반적으로 설명과 축이 데이터와 경쟁하지 않고 추가 컨텍스트를 제공하도록 하면서 데이터 자체를 가장 두드러지게 합니다.
>




**In a compact environment, maximize the width of the plot area to give people enough space to comfortably examine a chart.** To help important data fit well in a given width, ensure that labels on a vertical axis are as short as possible without losing clarity. You might also consider describing units in other areas of the chart, such as in a title, and placing a longer axis label, such as a category name, inside the plot area when doing so doesn’t obscure important information.
> 컴팩트한 환경에서는 그림 영역의 너비를 최대화하여 사람들이 차트를 편안하게 검토할 수 있는 충분한 공간을 확보하십시오. 중요한 데이터가 주어진 너비에 잘 맞도록 하려면 수직 축의 레이블이 선명도를 잃지 않고 가능한 한 짧아야 합니다. 또한 제목과 같은 차트의 다른 영역에 단위를 설명하고 그래프 영역 내에 범주 이름과 같은 긴 축 레이블을 배치하는 것이 중요한 정보를 모호하게 하지 않을 수도 있습니다.
>




