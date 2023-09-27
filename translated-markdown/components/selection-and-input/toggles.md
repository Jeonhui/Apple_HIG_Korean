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




**In general, don't replace a checkbox with a switch.** If you're already using a checkbox in your interface, it's probably best to keep using it.
> 일반적으로 확인란을 스위치로 바꾸지 마십시오. 인터페이스에서 확인란을 이미 사용하고 있다면 계속 사용하는 것이 가장 좋습니다.
>




### **Checkboxes**

A checkbox is a small square button that’s empty when the button is off, contains a checkmark when the button is on, and can contain a dash when the button’s state is mixed. Unless a checkbox appears in a checklist, a descriptive label follows the button.
> 확인란은 단추가 꺼져 있을 때 비어 있고 단추가 켜져 있을 때 확인 표시가 있으며 단추 상태가 혼합되어 있을 때 대시가 포함될 수 있는 작은 사각형 단추입니다. 체크리스트에 확인란이 나타나지 않는 한 설명 레이블이 버튼 뒤에 나타납니다.
>




**Use a checkbox instead of a switch if you need to present a hierarchy of settings.** The visual style of checkboxes helps them align well and communicate grouping. By using alignment — generally along the leading edge of the checkboxes — and indentation, you can show dependencies, such as when the state of a checkbox governs the state of subordinate checkboxes.
> 설정 계층을 표시해야 하는 경우 스위치 대신 확인란을 사용하십시오. 확인란의 시각적 스타일은 확인란을 잘 정렬하고 그룹화를 전달하는 데 도움이 됩니다. 정렬(일반적으로 확인란의 앞 가장자리를 따라) 및 들여쓰기를 사용하여 확인란 상태가 하위 확인란 상태를 지배하는 경우와 같은 종속성을 표시할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/toggles/images/checkbox-alignment.svg](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/toggles/images/checkbox-alignment.svg)

**Consider using radio buttons if you need to present a set of more than two mutually exclusive options.** When people need to choose from options in addition to just “on” or “off,” using multiple radio buttons can help you clarify each option with a unique label.
> 두 개 이상의 상호 배타적 옵션 집합을 표시해야 하는 경우 라디오 단추를 사용하는 것을 고려하십시오. 사람들이 "켜기" 또는 "끄기" 외에 옵션을 선택해야 할 때 여러 라디오 단추를 사용하면 고유한 레이블을 사용하여 각 옵션을 명확하게 지정할 수 있습니다.
>




**Consider using a label to introduce a group of checkboxes if their relationship isn't clear.** Describe the set of options, and align the label’s baseline with the first checkbox in the group.
> 레이블의 관계가 명확하지 않은 경우 레이블을 사용하여 확인란 그룹을 도입하는 것을 고려해 보십시오. 옵션 집합을 설명하고 레이블의 기준선을 그룹의 첫 번째 확인란에 맞춥니다.
>




**Accurately reflect a checkbox’s state in its appearance.** A checkbox can be selected, deselected, or mixed. If you use a checkbox to globally enable and disable multiple subordinate checkboxes, show a mixed state when the subordinate checkboxes have different states. For example, you might need to present a text-style setting that turns all styles on or off, but also lets people choose a subset of individual style settings like bold, italic, or underline. For developer guidance, see [allowsMixedState](https://developer.apple.com/documentation/appkit/nsbutton/1528670-allowsmixedstate).
> 확인란의 상태를 모양에 정확하게 반영합니다. 확인란을 선택하거나 선택 취소하거나 혼합할 수 있습니다. 확인란을 사용하여 여러 하위 확인란을 전체적으로 사용하거나 사용하지 않도록 설정하는 경우 하위 확인란의 상태가 다를 때 혼합 상태를 표시합니다. 예를 들어, 모든 스타일을 설정하거나 해제하는 텍스트 스타일 설정을 제공해야 하지만 굵게, 기울임꼴 또는 밑줄과 같은 개별 스타일 설정의 하위 집합을 선택할 수도 있습니다. 개발자 지침은 혼합 상태 허용을 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/toggles/images/checkbox-deselected.svg](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/toggles/images/checkbox-deselected.svg)

Deselected

![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/toggles/images/checkbox-selected.svg](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/toggles/images/checkbox-selected.svg)

Selected

![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/toggles/images/checkbox-mixed.svg](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/toggles/images/checkbox-mixed.svg)

Mixed

### **Radio buttons**

A radio button is a small, circular button followed by a label. Typically displayed in groups of two to five, radio buttons present a set of mutually exclusive choices.
> 라디오 버튼은 라벨 뒤에 오는 작고 둥근 버튼이다. 일반적으로 두 개에서 다섯 개의 그룹으로 표시되는 라디오 버튼은 상호 배타적인 선택 세트를 나타냅니다.
>




A radio button’s state is either on (a filled circle) or off (an empty circle). Although a radio button can also display a mixed state (indicated by a dash), this state is rarely useful because you can communicate multiple states by using additional radio buttons. If you need to show that a setting or item has a mixed state, consider using a checkbox instead.
> 라디오 버튼의 상태는 on(채운 원) 또는 off(빈 원)입니다. 라디오 단추는 대시로 표시되는 혼합 상태도 표시할 수 있지만, 추가 라디오 단추를 사용하여 여러 상태를 통신할 수 있기 때문에 이 상태는 거의 유용하지 않습니다. 설정 또는 항목의 상태가 혼합되어 있음을 표시해야 하는 경우 대신 확인란을 사용하는 것이 좋습니다.
>




**Prefer a set of radio buttons to present mutually exclusive options.** If you need to let people choose multiple options in a set, use checkboxes instead.
> 라디오 단추 집합을 사용하여 서로 배타적인 옵션을 표시합니다. 사용자가 한 집합에서 여러 옵션을 선택할 수 있도록 하려면 대신 확인란을 사용하십시오.
>




**Avoid listing too many radio buttons in a set.** A long list of radio buttons takes up a lot of space in the interface and can be overwhelming. If you need to present more than about five options, consider using a component like a [pop-up button](../components/menus-and-actions/pop-up-buttons) instead.
> 라디오 단추를 너무 많이 나열하지 마십시오. 라디오 단추의 긴 목록은 인터페이스에서 많은 공간을 차지하고 압도적일 수 있습니다. 다섯 가지 이상의 옵션을 제시해야 하는 경우 팝업 버튼과 같은 구성 요소를 대신 사용하는 것을 고려해 보십시오.
>




**To present a single setting that can be on or off, prefer a checkbox.**Although a single radio button can also turn something on or off, the presence or absence of the checkmark in a checkbox can make the current state easier to understand at a glance. In rare cases where a single checkbox doesn’t clearly communicate the opposing states, you can use a pair of radio buttons, each with a label that specifies the state it controls.
> 켜거나 끌 수 있는 단일 설정을 표시하려면 확인란을 선택합니다.단일 라디오 버튼으로도 무언가를 켜거나 끌 수 있지만 확인란에 체크 표시가 있는지 여부를 확인하면 현재 상태를 한 눈에 쉽게 이해할 수 있습니다. 단일 확인란이 서로 반대되는 상태를 명확하게 전달하지 않는 드문 경우에는 각각 제어하는 상태를 지정하는 레이블이 있는 라디오 단추를 사용할 수 있습니다.
>




**Use consistent spacing when you display radio buttons horizontally.**Measure the space needed to accommodate the longest button label, and use that measurement consistently.
> 라디오 단추를 수평으로 표시할 때는 일정한 간격을 사용합니다.가장 긴 버튼 레이블을 수용하는 데 필요한 공간을 측정하고 해당 측정값을 일관되게 사용합니다.
>



