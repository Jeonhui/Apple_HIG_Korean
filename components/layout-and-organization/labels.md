# **[components-layout-and-organization] labels**

## A label is a static piece of text that people can read and often copy, but not edit.
> 레이블은 사람들이 읽을 수 있고 종종 복사할 수 있지만 편집할 수는 없는 정적 텍스트입니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/label-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/label-intro-dark_2x.png)

Labels display text throughout the interface, in buttons, menu items, and views, helping people understand the current context and what they can do next.
> 레이블은 인터페이스 전체, 단추, 메뉴 항목 및 보기에 텍스트를 표시하여 사람들이 현재 컨텍스트와 다음에 수행할 수 있는 작업을 이해하는 데 도움이 됩니다.
>




The term *label* refers to uneditable text that can appear in various places. For example:
> 레이블이라는 용어는 다양한 위치에 나타날 수 있는 편집 불가능한 텍스트를 나타냅니다. 예:
>




- Within a button, a label generally conveys what the button does, such as Edit, Cancel, or Send.
- >  단추 내에서 레이블은 일반적으로 편집, 취소 또는 전송과 같이 단추가 수행하는 작업을 전달합니다.

- Within many lists, a label can describe each item, often accompanied by a symbol or an image.
- >  많은 목록에서 라벨은 종종 기호나 이미지를 동반하는 각 항목을 설명할 수 있다.

- Within a view, a label might provide additional context by introducing a control or describing a common action or task that people can perform in the view.
- >  뷰 내에서 레이블은 컨트롤을 도입하거나 사용자가 뷰에서 수행할 수 있는 공통 작업 또는 작업을 설명하여 추가 컨텍스트를 제공할 수 있습니다.


**DEVELOPER NOTE**To display uneditable text, SwiftUI defines two components: [Label](https://developer.apple.com/documentation/swiftui/label) and [Text](https://developer.apple.com/documentation/swiftui/text).
> 편집할 수 없는 텍스트를 표시하는 개발자 참고, SwiftUI는 레이블과 텍스트의 두 가지 구성 요소를 정의합니다.
>




The guidance below can help you use a label to display text. In some cases, guidance for specific components — such as [buttons](../components/menus-and-actions/buttons), [menus](../components/menus-and-actions/menus), and [lists](../components/layout-and-organization/lists-and-tables) — includes additional recommendations for using text.
> 아래 지침은 레이블을 사용하여 텍스트를 표시하는 데 도움이 될 수 있습니다. 경우에 따라 단추, 메뉴 및 목록과 같은 특정 구성요소에 대한 지침에는 텍스트 사용에 대한 추가 권장 사항이 포함되어 있습니다.
>




# **Best practices**

**Use a label to display a small amount of text that people don’t need to edit.** If you need to let people edit a small amount of text, use a [text field](../components/selection-and-input/text-fields). If you need to display a large amount of text, and optionally let people edit it, use a [text view](../components/content/text-views).
> 사용자가 편집할 필요가 없는 소량의 텍스트를 표시하려면 레이블을 사용합니다. 사용자가 소량의 텍스트를 편집할 수 있도록 하려면 텍스트 필드를 사용하십시오. 많은 양의 텍스트를 표시하고 선택적으로 사용자가 편집할 수 있도록 하려면 텍스트 보기를 사용하십시오.
>




**Prefer system fonts.** A label can display plain or styled text, and it supports Dynamic Type (where available) by default. If you adjust the style of a label or use custom fonts, make sure the text remains legible.
> 시스템 글꼴 선호. 레이블은 일반 또는 스타일링된 텍스트를 표시할 수 있으며 기본적으로 동적 유형(사용 가능한 경우)을 지원합니다. 레이블의 스타일을 조정하거나 사용자 정의 글꼴을 사용하는 경우 텍스트를 읽을 수 있는 상태로 유지해야 합니다.
>




**Use system-provided label colors to communicate relative importance.**The system defines four label colors that vary in appearance to help you give text different levels of visual importance. For additional guidance, see [Color](../foundations/color).
> 시스템에서 제공한 레이블 색상을 사용하여 상대적 중요도를 전달하십시오.시스템은 텍스트에 다양한 시각적 중요도를 부여할 수 있도록 모양에 따라 다른 네 가지 레이블 색상을 정의합니다. 자세한 내용은 색상을 참조하십시오.
>




| System color | Example usage | iOS, iPadOS, tvOS | macOS |
| --- | --- | --- | --- |
| Label | Primary information | labelColor | labelColor |
| Secondary label | A subheading or supplemental text | secondaryLabelColor | secondaryLabelColor |
| Tertiary label | Text that describes an unavailable item or behavior | tertiaryLabelColor | tertiaryLabelColor |
| Quaternary label | Watermark text | quaternaryLabelColor | quaternaryLabelColor |

**Make useful label text selectable.** If a label contains useful information — like an error message, a location, or an IP address — consider letting people select and copy it for pasting elsewhere.
> 유용한 레이블 텍스트를 선택할 수 있습니다. 라벨은 오류 메시지, 위치, 위치, 위치, IP 주소, IP 주소, 다른 다른 다른 다른 다른 다른 다른 다른 다른 다른 다른 다른 다른 다른 다른 다른 다른 다른 다른 다른 다른 다른 다른 다른
>




# **Platform considerations**

*No additional considerations for iOS, iPadOS, or tvOS.*
> iOS, iPadOS 또는 tvOS에 대한 추가 고려 사항 없음.
>




# **macOS**

**DEVELOPER NOTE**To display uneditable text in a label, use the [isEditable](https://developer.apple.com/documentation/appkit/nstextfield/1399407-iseditable) property of [NSTextField](https://developer.apple.com/documentation/appkit/nstextfield).
> 개발자 참고: 편집 불가능한 텍스트를 레이블에 표시하려면 NSTextField의 isEditable 속성을 사용하십시오.
>




# **watchOS**

In addition to using SwiftUI [Label](https://developer.apple.com/documentation/swiftui/label) and [Text](https://developer.apple.com/documentation/swiftui/text) components in your watchOS app, you can use WatchKit date and timer labels to display real-time values.
> Swift 사용 외에도시계의 UI 레이블 및 텍스트 구성 요소OS 앱에서 WatchKit 날짜 및 타이머 라벨을 사용하여 실시간 값을 표시할 수 있습니다.
>




A [date label](https://developer.apple.com/documentation/watchkit/wkinterfacedate) (shown below on the left) displays the current date, the current time, or a combination of both. You can configure a date label to use a variety of formats, calendars, and time zones. After configuration, a date label updates its value without further input from your app. A [timer label](https://developer.apple.com/documentation/watchkit/wkinterfacetimer) (shown below on the right) displays a precise countdown or count-up timer. You can configure a timer label to display its count value in a variety of formats. After configuration, a timer label counts down or up without further input from your app.
> 날짜 레이블(왼쪽 아래 표시)은 현재 날짜, 현재 시간 또는 둘의 조합을 표시합니다. 다양한 형식, 달력 및 표준시를 사용하도록 날짜 레이블을 구성할 수 있습니다. 구성 후 날짜 라벨은 앱에서 추가 입력 없이 해당 값을 업데이트합니다. 타이머 라벨(오른쪽 아래 표시)은 정확한 카운트다운 또는 카운트업 타이머를 표시합니다. 타이머 레이블을 구성하여 카운트 값을 다양한 형식으로 표시할 수 있습니다. 구성 후 타이머 라벨은 앱에서 추가 입력 없이 카운트다운하거나 카운트업합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/labels/images/dates-timers-mail_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/labels/images/dates-timers-mail_2x.png)

Date label

![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/labels/images/dates-timers-stopwatch_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/labels/images/dates-timers-stopwatch_2x.png)

Timer label

**Consider using date and timer labels in complications.** When you use the system-provided date and timer labels, watchOS automatically adjusts the presentation of the label content to fit the available space. For guidance, see [Complications](../components/system-experiences/complications); for developer guidance, see [CLKRelativeDateTextProvider](https://developer.apple.com/documentation/clockkit/clkrelativedatetextprovider).
> 복잡한 경우 날짜 및 타이머 라벨을 사용하는 것을 고려하십시오. 시스템에서 제공하는 날짜 및 타이머 라벨을 사용할 경우,OS는 사용 가능한 공간에 맞게 라벨 콘텐츠의 표시를 자동으로 조정합니다. 자세한 내용은 합병증을 참조하십시오. 개발자 지침은 CLKRelativeDateTextProvider를 참조하십시오.
>



