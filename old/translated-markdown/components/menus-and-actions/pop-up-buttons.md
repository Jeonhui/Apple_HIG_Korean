# **[components-menus-and-actions] pop-up-buttons**

## A pop-up button displays a menu of mutually exclusive options.
> 팝업 단추는 상호 배타적인 옵션 메뉴를 표시합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/popup-button-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/popup-button-intro-dark_2x.png)

After people choose an item from a pop-up button’s menu, the menu closes, and the button can update its content to indicate the current selection.
> 팝업 단추의 메뉴에서 항목을 선택하면 메뉴가 닫히고, 단추가 현재 선택 항목을 나타내도록 내용을 업데이트할 수 있습니다.
>




# **Best practices**

**Use a pop-up button to present a flat list of mutually exclusive options or states.** A pop-up button helps people make a choice that affects their content or the surrounding view. Use a [pull-down button](../components/menus-and-actions/pull-down-buttons) instead if you need to:
> 팝업 단추를 사용하여 상호 배타적인 옵션 또는 상태 목록을 표시할 수 있습니다. 팝업 단추는 사람들이 콘텐츠나 주변 보기에 영향을 미치는 선택을 하도록 도와줍니다. 필요한 경우 풀다운 버튼을 대신 사용하십시오.
>




- Offer a list of actions
- >  작업 목록 제공

- Let people select multiple items
- >  사용자가 여러 항목을 선택하도록 허용

- Include a submenu

**Provide a useful default selection.** A pop-up button can update its content to identify the current selection, but if people haven’t made a selection yet, it shows the default item you specify. When possible, make the default selection an item that most people are likely to want.
> 유용한 기본 선택 항목을 제공합니다. 팝업 단추는 내용을 업데이트하여 현재 선택 항목을 식별할 수 있지만, 사용자가 아직 선택하지 않은 경우 사용자가 지정한 기본 항목을 표시합니다. 가능한 경우 기본 선택을 대부분의 사용자가 원할 가능성이 높은 항목으로 만듭니다.
>




**Give people a way to predict a pop-up button’s options without opening it.** For example, you can use an introductory label or a button label that describes the button’s effect, giving context to the options.
> 예를 들어, 단추의 효과를 설명하는 소개 레이블이나 단추 레이블을 사용하여 옵션에 대한 컨텍스트를 제공할 수 있습니다.
>




**Consider using a pop-up button when space is limited and you don’t need to display all options all the time.** Pop-up buttons are a space-efficient way to present a wide array of choices.
> 공간이 제한되어 있고 항상 모든 옵션을 표시할 필요가 없는 경우 팝업 단추를 사용하는 것이 좋습니다. 팝업 단추는 다양한 선택 항목을 표시할 수 있는 공간 효율적인 방법입니다.
>




**If necessary, include a Custom option in a pop-up button’s menu to provide additional items that are useful in some situations.** Offering a Custom option can help you avoid cluttering the interface with items or controls that people need only occasionally. You can also display explanatory text below the list to help people understand how the options work.
> 필요한 경우 팝업 단추의 메뉴에 사용자 지정 옵션을 포함하면 일부 상황에서 유용한 추가 항목을 제공할 수 있습니다. 사용자 지정 옵션을 제공하면 사용자가 가끔만 필요한 항목이나 컨트롤로 인터페이스를 복잡하게 만들지 않도록 할 수 있습니다. 또한 목록 아래에 설명 텍스트를 표시하여 선택사항이 어떻게 작동하는지 이해할 수 있습니다.
>




# **Platform considerations**

*No additional considerations for iOS or macOS. Not supported in tvOS or watchOS.*
> iOS 또는 macOS에 대한 추가 고려 사항 없음. tvOS 또는 시계에서 지원되지 않음OS.
>




# **iPadOS**

**Within a popover or modal view, consider using a pop-up button instead of a disclosure indicator to present multiple options for a list item.** For example, people can quickly choose an option from the pop-up button’s menu without navigating to a detail view. Consider using a pop-up button in this scenario when you have a fairly small, well-defined set of options that work well in a menu.
> 팝업 또는 모달 보기에서 노출 표시기 대신 팝업 단추를 사용하여 목록 항목에 대한 여러 옵션을 표시하는 것을 고려해 보십시오. 예를 들어, 사용자는 세부 보기로 이동하지 않고 팝업 단추의 메뉴에서 옵션을 빠르게 선택할 수 있습니다. 메뉴에서 잘 작동하는 상당히 작고 잘 정의된 옵션 집합이 있는 경우 이 시나리오에서 팝업 단추를 사용하는 것을 고려해 보십시오.
>



