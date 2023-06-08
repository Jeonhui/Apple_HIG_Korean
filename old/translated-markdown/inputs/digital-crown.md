# **[inputs] digital-crown**

## The Digital Crown is the primary hardware input for all Apple Watch models.
> 디지털 크라운은 모든 Apple Watch 모델의 기본 하드웨어 입력입니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-digital-crown-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-digital-crown-intro_2x.png)

As people turn the Digital Crown, it generates information you can use to enhance or facilitate interactions with your app, like scrolling or operating standard or custom controls.
> 사람들이 디지털 크라운을 돌리면 스크롤 또는 조작 표준 또는 사용자 지정 컨트롤과 같은 앱과의 상호 작용을 향상하거나 촉진하는 데 사용할 수 있는 정보가 생성됩니다.
>




**NOTE**Apps don't respond to presses on the Digital Crown because watchOS reserves these interactions for system-provided functionality like revealing the Home Screen.
> 참고앱은 디지털 크라운을 눌러도 반응하지 않습니다. 왜냐하면 다음을 보기 때문입니다.OS는 홈 스크린을 공개하는 것과 같은 시스템 제공 기능을 위해 이러한 상호 작용을 예약합니다.
>




Apple Watch Series 4 and later provides haptic feedback for the Digital Crown, which gives people a more tactile experience as they scroll through content. By default, the system provides linear haptic *detents* — or taps — as people turn the Digital Crown a specific distance. Some system controls, like table views, provide detents as new items scroll onto the screen.
> 애플 워치 시리즈 4 이상은 디지털 크라운을 위한 햅틱 피드백을 제공하며, 이는 콘텐츠를 스크롤할 때 사람들에게 더 촉각적인 경험을 제공한다. 기본적으로 이 시스템은 사람들이 디지털 크라운을 특정 거리만큼 돌릴 때 선형 햅틱 멈춤(또는 탭)을 제공합니다. 테이블 보기와 같은 일부 시스템 컨트롤은 새 항목이 화면으로 스크롤될 때 멈춤 기능을 제공합니다.
>




# **Best practices**

**Provide visual feedback in response to Digital Crown interactions.** For example, pickers change the currently displayed value as people use the Digital Crown. If you track turns directly, use this data to update your interface programmatically. If you don’t provide visual feedback, people are likely to assume that turning the Digital Crown has no effect in your app.
> 디지털 크라운 상호 작용에 대한 시각적 피드백을 제공합니다. 예를 들어, 피커는 사람들이 디지털 크라운을 사용할 때 현재 표시되는 값을 변경합니다. 회전을 직접 추적하는 경우 이 데이터를 사용하여 인터페이스를 프로그래밍 방식으로 업데이트하십시오. 시각적 피드백을 제공하지 않으면 사람들은 당신의 앱에서 디지털 크라운을 돌리는 것이 아무런 효과가 없다고 생각할 가능성이 높다.
>




**Update your interface to match the speed with which people turn the Digital Crown.** People expect turning the Digital Crown to give them precise control over an interface, so it works well to use this speed to determine the speed at which you make changes. Avoid updating content at a rate that makes it difficult for people to select values.
> 사람들이 디지털 크라운을 돌리는 속도에 맞춰 인터페이스를 업데이트합니다. 사람들은 디지털 크라운을 돌리면 인터페이스를 정확하게 제어할 수 있기를 기대하기 때문에 이 속도를 사용하여 변경하는 속도를 결정하는 것이 좋습니다. 사용자가 값을 선택하기 어려운 속도로 내용을 업데이트하지 않도록 합니다.
>




**Use the default haptic feedback when it makes sense in your app.** If haptic feedback doesn't feel right in the context of your app — for example, if the default detents don’t match your app’s animation — disable the detents. You can also adjust the haptic feedback behavior for tables, letting them use linear detents instead of row-based detents. For example, if your table has rows with significantly different heights, linear detents may give people a more consistent experience.
> 앱에서 적합할 때 기본 햅틱 피드백을 사용하십시오. 앱의 컨텍스트에서 햅틱 피드백이 올바르게 느껴지지 않으면(예: 기본 멈춤쇠가 앱의 애니메이션과 일치하지 않는 경우) 멈춤쇠를 사용하지 않도록 설정하십시오. 또한 테이블에 대한 햅틱 피드백 동작을 조정하여 행 기반 멈춤쇠 대신 선형 멈춤쇠를 사용할 수 있습니다. 예를 들어, 표의 높이가 유의하게 다른 행이 있는 경우 선형 멈춤쇠는 사용자에게 보다 일관된 경험을 제공할 수 있습니다.
>




# **Platform considerations**

*Not supported in iOS, iPadOS, macOS, or tvOS.*
> iOS, iPadOS, macOS 또는 tvOS에서는 지원되지 않습니다.
>



