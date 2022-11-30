# **[components-status] gauges**

## A gauge displays a specific numerical value within a range of values.
> 게이지는 값 범위 내에서 특정 수치를 표시합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/gauges-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/gauges-intro-dark_2x.png)

In addition to indicating the current value in a range, a gauge can provide more context about the range itself. For example, a temperature gauge can use text to identify the highest and lowest temperatures in the range and display a spectrum of colors that visually reinforce the changing values.
> 게이지는 범위의 현재 값을 표시할 뿐만 아니라 범위 자체에 대한 더 많은 컨텍스트를 제공할 수 있습니다. 예를 들어, 온도 게이지는 텍스트를 사용하여 범위에서 가장 높은 온도와 가장 낮은 온도를 식별하고 변화하는 값을 시각적으로 보강하는 색상의 스펙트럼을 표시할 수 있다.
>




# **Anatomy**

A gauge uses a circular or linear path to represent a range of values, mapping the current value to a specific point on the path. A standard gauge displays an indicator that shows the current value’s location; a gauge that uses the capacity style displays a fill that stops at the value’s location on the path.
> 게이지는 원형 또는 선형 경로를 사용하여 값 범위를 나타내며 현재 값을 경로의 특정 지점에 매핑합니다. 표준 게이지는 현재 값의 위치를 표시하는 표시기를 표시하고, 용량 스타일을 사용하는 게이지는 경로의 값 위치에 정지하는 채우기를 표시합니다.
>




Circular and linear gauges in both standard and capacity styles are also available in a variant that’s visually similar to watchOS complications. This variant — called accessory — works well in iOS Lock Screen widgets and anywhere you want to echo the appearance of complications.
> 표준 및 용량 스타일의 원형 및 선형 게이지도 시계와 시각적으로 유사한 변형으로 사용할 수 있습니다.운영 체제의 복잡성. 액세서리라고 불리는 이 변형은 iOS 잠금 화면 위젯과 복잡한 모양을 반영하고 싶은 모든 곳에서 잘 작동합니다.
>




**NOTE**In addition to gauges, macOS also supports level indicators, some of which have visual styles that are similar to gauges. For guidance, see [macOS](https://developer.apple.com/design/human-interface-guidelines/components/status/gauges#macos).
> 참고 게이지 외에도 MacOS는 레벨 표시기도 지원하며, 일부는 게이지와 유사한 시각적 스타일을 가지고 있습니다. 자세한 내용은 macOS를 참조하십시오.
>




# **Best practices**

**Write succinct labels that describe the current value and both endpoints of the range.** Although not every gauge style displays all labels, VoiceOver reads the visible labels to help people understand the gauge without seeing the screen.
> 현재 값과 범위의 두 끝점을 모두 설명하는 간결한 레이블을 작성합니다. 모든 게이지 스타일이 모든 레이블을 표시하는 것은 아니지만, VoiceOver는 표시되는 레이블을 읽어 사람들이 화면을 보지 않고 게이지를 이해하도록 도와줍니다.
>




**Consider filling the path with a gradient to help communicate the purpose of the gauge.** For example, a temperature gauge might use colors that range from red to blue to represent temperatures that range from hot to cold.
> 게이지의 목적을 전달하는 데 도움이 되는 그라데이션으로 경로를 채우는 것을 고려하십시오. 예를 들어, 온도 게이지는 고온에서 저온에 이르는 온도를 나타내기 위해 빨간색에서 파란색 범위의 색상을 사용할 수 있습니다.
>




# **Platform considerations**

