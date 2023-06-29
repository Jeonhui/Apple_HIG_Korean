# **[components-selection-and-input] steppers**

## A stepper is a two-segment control that people use to increase or decrease an incremental value.
> 스테퍼는 사람들이 증분 값을 증가시키거나 감소시키기 위해 사용하는 2 세그먼트 컨트롤입니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/stepper-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/stepper-intro-dark_2x.png)

A stepper sits next to a field that displays its current value, because the stepper itself doesn't display a value.
> 스테퍼 자체는 값을 표시하지 않으므로 스테퍼는 현재 값을 표시하는 필드 옆에 있습니다.
>




# **Best practices**

**Make the value that a stepper affects obvious.** A stepper itself doesn’t display any values, so make sure people know which value they’re changing when they use a stepper.
> 스테퍼가 영향을 미치는 값을 명확하게 합니다. 스테퍼 자체에는 값이 표시되지 않으므로 스테퍼를 사용할 때 사람들이 어떤 값을 변경하고 있는지 확실히 알 수 있습니다.
>




**Consider pairing a stepper with a text field when large value changes are likely.** Steppers work well by themselves for making small changes that require a few taps or clicks. By contrast, people appreciate the option to use a field to enter specific values, especially when the values they use can vary widely. On a printing screen, for example, it can help to have both a stepper and a text field to set the number of copies.
> 큰 값이 변경될 가능성이 있을 때는 스테퍼를 텍스트 필드와 페어링하는 것을 고려하십시오. 스테퍼는 몇 번의 탭이나 클릭이 필요한 작은 변경을 수행하는 데 적합합니다. 대조적으로, 사람들은 특히 그들이 사용하는 값이 매우 다양할 수 있는 경우 특정 값을 입력하기 위해 필드를 사용하는 옵션을 높이 평가한다. 예를 들어 인쇄 화면에서는 복사본 수를 설정하기 위해 스테퍼와 텍스트 필드를 모두 사용할 수 있습니다.
>




# **Platform considerations**

*No additional considerations for iOS or iPadOS. Not supported in watchOS or tvOS.*
> iOS 또는 iPadOS에 대한 추가 고려 사항은 없습니다. 워치에서 지원되지 않음OS 또는 TVOS.
>




# **macOS**

**For large value ranges, consider enabling Shift-click to change the value quickly.** If your app benefits from larger changes in a stepper’s value, it can be useful to let people Shift-click the stepper to change the value by more than the default increment (by 10 times the default, for example).
> 큰 값 범위의 경우 Shift-click을 활성화하여 값을 빠르게 변경하는 것을 고려하십시오. 앱이 스테퍼 값의 더 큰 변경으로 인해 혜택을 받는 경우, 사람들이 Shift-click을 통해 기본 증분(예: 기본값의 10배) 이상 값을 변경하도록 하는 것이 유용할 수 있습니다.
>



