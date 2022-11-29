# **[components-selection-and-input] toggles**

## A toggle lets people choose between a pair of opposing states, like on and off, using a different appearance to indicate each state.
> 토글은 사람들이 각각의 상태를 나타내기 위해 다른 모양을 사용하여 켜짐과 꺼짐과 같은 한 쌍의 반대 상태 사이에서 선택할 수 있게 해준다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/toggles-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/toggles-intro-dark_2x.png)

Different platforms can support various toggle [styles](https://developer.apple.com/documentation/swiftui/togglestyle). For example, iOS, iPadOS, macOS, and watchOS support the switch toggle style, whereas only macOS supports the checkbox style.
> 플랫폼마다 다양한 토글 스타일을 지원할 수 있습니다. 예를 들어 iOS, iPadOS, macOS, watch 등이 있습니다.OS는 스위치 토글 스타일을 지원하는 반면, macOS만 확인란 스타일을 지원한다.
>




In addition, all platforms support buttons that enable toggle behavior by using a different appearance for each state.
> 또한 모든 플랫폼은 각 상태에 대해 다른 모양을 사용하여 토글 동작을 가능하게 하는 버튼을 지원합니다.
>




# **Best practices**

**Use a toggle to help people choose between two opposing values that affect the state of content or a view.** A toggle always lets people manage the state of something, so if you need to enable other types of actions — such as choosing from a list of items — use a different component, like a [pop-up button](../components/menus-and-actions/pop-up-buttons).
> 토글은 사용자가 콘텐츠 또는 보기 상태에 영향을 미치는 두 개의 상반된 값 중 하나를 선택할 수 있도록 도와줍니다. 토글은 항상 사용자가 무언가의 상태를 관리할 수 있도록 합니다. 따라서 항목 목록에서 선택하는 것과 같은 다른 유형의 작업을 활성화해야 하는 경우 팝업 단추와 같은 다른 구성 요소를 사용합니다.
>




**Clearly identify the setting, view, or content the toggle affects.** In general, the surrounding context provides enough information for people to understand what they’re turning on or off. In some cases, often in macOS apps, you can also supply a label to describe the state the toggle controls. If you use a button that behaves like a toggle, you generally use an interface icon that communicates its purpose, and you update its appearance — typically by changing the background — based on the current state.
> 토글이 영향을 미치는 설정, 보기 또는 내용을 명확하게 식별합니다. 일반적으로 주변 컨텍스트는 사용자가 설정하거나 해제하는 내용을 이해하기에 충분한 정보를 제공합니다. 경우에 따라 종종 macOS 앱에서 토글이 제어하는 상태를 설명하는 레이블을 제공할 수도 있습니다. 토글처럼 동작하는 단추를 사용하는 경우 일반적으로 용도를 나타내는 인터페이스 아이콘을 사용하고 현재 상태에 따라 배경을 변경하여 모양을 업데이트합니다.
>




**Make sure the visual differences in a toggle’s state are obvious.** For example, you might add or remove a color fill, show or hide the background shape, or change the inner details you display — like a checkmark or dot — to show that a toggle is on or off. Avoid relying solely on different colors to communicate state, because not everyone can perceive the differences.
> 예를 들어 색 채우기를 추가하거나 제거하거나 배경 모양을 표시하거나 숨기거나 체크 표시나 점과 같이 표시하는 내부 세부 정보를 변경하여 토글이 켜져 있는지 또는 꺼져 있는지 확인합니다. 모든 사람이 차이점을 인식할 수 있는 것은 아니기 때문에 상태를 전달하기 위해 다른 색에만 의존하는 것을 피하십시오.
>




# **Platform considerations**

*No additional considerations for tvOS or watchOS.*
> TVOS 또는 시계에 대한 추가 고려 사항 없음운영 체제
>




# **iOS, iPadOS**

**Use the switch toggle style only in a list row.** You don’t need to supply a label in this situation because the content in the row provides the context for the state the switch controls.
> 목록 행에서만 스위치 토글 스타일을 사용하십시오. 이 경우 행의 내용이 스위치가 제어하는 상태에 대한 컨텍스트를 제공하므로 레이블을 제공할 필요가 없습니다.
>




**Change the default color of a switch only if necessary.** The default green color tends to work well in most cases, but you might want to use your app’s accent color instead. Be sure to use a color that provides enough contrast with the uncolored appearance to be perceptible.
> 대부분의 경우 기본 녹색이 잘 작동하는 경향이 있지만 앱의 액센트 색을 대신 사용할 수도 있습니다. 색이 없는 외관과 충분히 대비가 되는 색상을 사용해야 합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/toggles/images/switches-default_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/toggles/images/switches-default_2x.png)

**Outside of a list, use a button that behaves like a toggle, not a switch.**Avoid supplying a label that explains the button’s purpose. The interface icon you create — combined with the alternative background appearances you supply — help people understand what the button does. For developer guidance, see [changesSelectionAsPrimaryAction](https://developer.apple.com/documentation/uikit/uibutton/3752184-changesselectionasprimaryaction/).
> 목록 밖에서는 스위치가 아닌 토글처럼 작동하는 단추를 사용합니다.버튼의 용도를 설명하는 레이블을 제공하지 마십시오. 사용자가 작성한 인터페이스 아이콘은 사용자가 제공하는 대체 배경 모양과 결합되어 단추의 기능을 이해하는 데 도움이 됩니다. 개발자 지침은 변경 사항을 참조하십시오.기본 작업으로 선택합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/toggles/images/toggle-button-on_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/toggles/images/toggle-button-on_2x.png)

Calendar displays a solid background shape behind the toggle’s symbol to indicate that the day’s events are visible.
> 달력은 토글 기호 뒤에 실시간 배경 모양을 표시하여 그날의 이벤트를 볼 수 있음을 나타냅니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/toggles/images/toggle-button-off_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/toggles/images/toggle-button-off_2x.png)

Calendar removes the solid background shape from the toggle to indicate that the day’s events are hidden.
> 일정관리는 토글에서 실시간 배경 모양을 제거하여 해당 날짜의 이벤트가 숨겨져 있음을 나타냅니다.
>




# **macOS**

In addition to the switch toggle style, macOS supports the checkbox style and also defines radio buttons that can provide similar behaviors.
> 스위치 토글 스타일 외에도 macOS는 체크박스 스타일을 지원하며 유사한 동작을 제공할 수 있는 라디오 버튼을 정의합니다.
>




**Use switches, checkboxes, and radio buttons in the window body, not the window frame.** In particular, avoid using these components in a toolbar or status bar.
> 창 프레임이 아닌 창 본문의 스위치, 확인란 및 라디오 버튼을 사용하십시오. 특히 도구 모음이나 상태 표시줄에서 이러한 구성 요소를 사용하지 마십시오.
>




### **Switches**

**Avoid using a switch to control a single detail or a minor setting.** A switch has more visual weight than a checkbox, so it looks better when it controls more functionality than a checkbox typically does. For example, you might use a switch to let people turn on or off a group of settings, instead of just one setting.
> 스위치를 사용하여 단일 세부 정보 또는 사소한 설정을 제어하지 마십시오. 스위치는 확인란보다 시각적 무게가 더 크기 때문에 확인란이 일반적으로 제어하는 것보다 더 많은 기능을 제어할 때 더 보기 좋습니다. 예를 들어 스위치를 사용하여 한 가지 설정 대신 설정 그룹을 켜거나 끌 수 있습니다.
>




