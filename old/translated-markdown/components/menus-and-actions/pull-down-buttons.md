# **[components-menus-and-actions] pull-down-buttons**

## A pull-down button displays a menu of items or actions that directly relate to the button’s purpose.
> 풀다운 단추는 단추의 용도와 직접 관련된 항목 또는 작업 메뉴를 표시합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/pulldown-button-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/pulldown-button-intro-dark_2x.png)

After people choose an item in a pull-down button’s menu, the menu closes, and the app performs the chosen action.
> 사람들이 풀다운 버튼의 메뉴에서 항목을 선택하면, 메뉴가 닫히고, 앱은 선택한 작업을 수행한다.
>




# **Best practices**

**Use a pull-down button to present commands or items that are directly related to the button’s action.** The menu lets you help people clarify the button’s target or customize its behavior without requiring additional buttons in your interface. For example:
> 풀다운 단추를 사용하여 단추의 동작과 직접 관련된 명령이나 항목을 표시할 수 있습니다. 메뉴를 사용하면 인터페이스에 단추를 추가하지 않고도 단추의 대상을 명확하게 지정하거나 단추의 동작을 사용자 지정할 수 있습니다. 예:
>




- An Add button could present a menu that lets people specify the item they want to add.
- >  추가 단추는 사용자가 추가할 항목을 지정할 수 있는 메뉴를 표시할 수 있습니다.

- A Sort button could use a menu to let people select an attribute on which to sort.
- >  정렬 단추는 사용자가 정렬할 속성을 선택할 수 있도록 메뉴를 사용할 수 있습니다.

- A Back button could let people choose a specific location to revisit instead of opening the previous one.
- >  뒤로 단추를 사용하면 이전 위치를 여는 대신 다시 방문할 특정 위치를 선택할 수 있습니다.


If you need to provide a list of mutually exclusive choices that aren’t commands, use a [pop-up button](../components/menus-and-actions/pop-up-buttons) instead.
> 명령이 아닌 상호 배타적 선택 목록을 제공해야 하는 경우 대신 팝업 단추를 사용하십시오.
>




**Avoid putting all of a view’s actions in one pull-down button.** A view’s primary actions need to be easily discoverable, so you don’t want to hide them in a pull-down button that people have to open before they can do anything.
> 보기의 모든 작업을 하나의 풀다운 단추에 넣지 마십시오. 보기의 기본 작업은 쉽게 검색할 수 있어야 하므로 사용자가 작업을 수행하기 전에 열어야 하는 풀다운 단추에 숨겨서는 안 됩니다.
>




**Balance menu length with ease of use.** Because people have to interact with a pull-down button before they can view its menu, listing a minimum of three items can help the interaction feel worthwhile. If you need to list only one or two items, consider using alternative components to present them, such as buttons to enable actions and toggles or switches to present selections. In contrast, listing too many items in a pull-down button’s menu can slow people down because it takes longer to find a specific item.
> 메뉴 길이와 사용 편의성의 균형을 맞추십시오. 사람들은 메뉴를 보기 전에 풀다운 버튼과 상호 작용해야 하기 때문에 최소 세 개의 항목을 나열하면 상호 작용이 가치 있다고 느낄 수 있습니다. 항목을 하나 또는 두 개만 나열해야 하는 경우 작업을 사용하도록 설정하는 단추나 선택 항목을 표시하도록 전환하는 단추와 같은 대체 구성 요소를 사용하는 것이 좋습니다. 반대로 풀다운 단추의 메뉴에 너무 많은 항목을 나열하면 특정 항목을 찾는 데 시간이 더 오래 걸리기 때문에 사람들의 속도가 느려질 수 있습니다.
>




**Display a succinct menu title only if it adds meaning.** In general, a pull-down button’s content — combined with descriptive menu items — provides all the context people need, making a menu title unnecessary.
> 일반적으로 풀다운 단추의 내용은 설명 메뉴 항목과 결합되어 필요한 모든 컨텍스트를 제공하므로 메뉴 제목이 필요하지 않습니다.
>




**Let people know when a pull-down button’s menu item is destructive, and ask them to confirm their intent.** Menus use red text to highlight actions that you identify as potentially destructive. When people choose a destructive action, the system displays an [action sheet](../components/presentation/action-sheets) (iOS) or [popover](../components/presentation/popovers)(iPadOS) in which they can confirm their choice or cancel the action. Because an action sheet appears in a different location from the menu and requires deliberate dismissal, it can help people avoid losing data by mistake.
> 풀다운 단추의 메뉴 항목이 파괴적인 경우 사용자에게 알려 의도를 확인하도록 요청합니다. 메뉴는 빨간색 텍스트를 사용하여 사용자가 잠재적으로 파괴적이라고 식별한 작업을 강조 표시합니다. 사람들이 파괴적인 행동을 선택하면, 시스템은 그들이 선택한 것을 확인하거나 그 행동을 취소할 수 있는 행동 시트(iOS) 또는 팝업(iPadOS)을 표시한다. 작업 시트는 메뉴와 다른 위치에 나타나며 고의적인 해제가 필요하기 때문에 실수로 데이터가 손실되는 것을 방지할 수 있습니다.
>




**Include an interface icon with a menu item when it provides value.** If you need to clarify an item’s meaning, you can display an [interface icon](../foundations/icons) or image after its label. Using an [SF Symbol](../foundations/sf-symbols) for this purpose can help you provide a familiar experience while ensuring that the symbol remains aligned with the text at every scale.
> 값을 제공할 때 메뉴 항목에 인터페이스 아이콘을 포함합니다. 항목의 의미를 명확히 해야 할 경우 인터페이스 아이콘이나 이미지를 레이블 뒤에 표시할 수 있습니다. 이 용도로 SF 기호를 사용하면 기호가 모든 축척에서 텍스트와 정렬되도록 하는 동시에 친숙한 경험을 제공하는 데 도움이 될 수 있습니다.
>




# **Platform considerations**

*No additional considerations for macOS. Not supported in tvOS or watchOS.*
> MacOS에 대한 추가 고려 사항은 없습니다. TVOS 또는 워치에서 지원되지 않음운영 체제
>




# **iOS, iPadOS**

**NOTE**You can also let people reveal a pull-down menu by performing a specific gesture on a button. For example, in iOS 14 and later, Safari responds to a touch and hold gesture on the Tabs button by displaying a menu of tab-related actions, like New Tab and Close All Tabs.
> 참고 단추에 특정 제스처를 수행하여 풀다운 메뉴를 표시할 수도 있습니다. 예를 들어 iOS 14 이상에서는 새 탭 및 모든 탭 닫기와 같은 탭 관련 작업의 메뉴를 표시하여 탭 단추의 터치 및 유지 제스처에 응답합니다.
>




**Consider using a More pull-down button to present items that don’t need prominent positions in the main interface.** A More button can help you offer a range of items where space is constrained, but it can also hinder discoverability. Although people generally understand that a More button offers additional functionality related to the current context, the ellipsis icon doesn’t necessarily help them predict its contents. To design an effective More button, weigh the convenience of its size against its impact on discoverability to find a balance that works in your app. Create a More button by using the `ellipsis.circle` symbol.
> 주 인터페이스에서 눈에 띄는 위치가 필요 없는 항목을 표시하려면 추가 풀다운 단추를 사용하십시오. 추가 단추는 공간이 제한된 항목을 제공하는 데 도움이 될 수 있지만 검색을 방해할 수도 있습니다. 사람들은 일반적으로 추가 단추가 현재 컨텍스트와 관련된 추가 기능을 제공한다는 것을 이해하지만 줄임표 아이콘이 내용을 예측하는 데 반드시 도움이 되는 것은 아닙니다. 효과적인 추가 버튼을 설계하려면 크기의 편리성을 검색 가능성에 미치는 영향과 비교하여 앱에서 작동하는 균형을 찾으십시오. "ellipsis.circle" 기호를 사용하여 추가 버튼을 만듭니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/pull-down-buttons/images/menu-secondary-actions_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/pull-down-buttons/images/menu-secondary-actions_2x.png)

Files uses a More pull-down button to offer actions — like adding a folder or scanning a document — in addition to options for viewing and sorting the content.
> 파일은 추가 풀다운 단추를 사용하여 내용 보기 및 정렬 옵션 외에 폴더 추가 또는 문서 검색과 같은 작업을 제공합니다.
>



