# **[content] text-views**

## A text view displays multiline, styled text content, which can optionally be editable.
> 텍스트 보기는 여러 줄의 스타일링된 텍스트 내용을 표시하며, 이 내용은 선택적으로 편집할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/text-view-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/text-view-intro-dark_2x.png)

Text views can be any height and enable scrolling when the content extends outside of the view. By default, content within a text view is aligned to the leading edge and uses the system label color. In iOS or iPadOS, if a text view is editable, a keyboard appears when people select the view.
> 텍스트 보기는 모든 높이가 될 수 있으며 내용이 보기 외부로 확장될 때 스크롤할 수 있습니다. 기본적으로 텍스트 뷰 내의 내용은 선행 에지에 정렬되며 시스템 레이블 색상을 사용합니다. iOS 또는 iPadOS에서 텍스트 보기를 편집할 수 있으면 사용자가 보기를 선택하면 키보드가 나타납니다.
>




# **Best practices**

**Use a text view when you need to display text that’s long, editable, or in a special format.** Text views differ from [text fields](../components/selection-and-input/text-fields) and [labels](../components/layout-and-organization/labels) in that they provide the most options for displaying specialized text and receiving text input. If you need to display a small amount of text, it’s simpler to use a label instead or a text field if the text is editable.
> 텍스트 보기는 길이가 길고 편집 가능하거나 특별한 형식으로 텍스트를 표시해야 할 때 사용합니다. 텍스트 보기는 전문 텍스트를 표시하고 텍스트 입력을 받을 수 있는 가장 많은 옵션을 제공한다는 점에서 텍스트 필드 및 레이블과 다릅니다. 소량의 텍스트를 표시해야 하는 경우 레이블을 대신 사용하거나 텍스트를 편집할 수 있는 경우 텍스트 필드를 사용하는 것이 더 간단합니다.
>




**Keep text legible.** Although you can use multiple fonts, colors, and alignments in creative ways, it’s essential to maintain the readability of your content. It’s a good idea to adopt Dynamic Type so your text still looks good if people change text size on their device. You should also test your content with accessibility options enabled, such as bold text. For guidance, see [Accessibility](../foundations/accessibility) and [Typography](../foundations/typography).
> 텍스트를 읽기 쉽게 유지합니다. 여러 글꼴, 색상 및 맞춤을 창의적인 방법으로 사용할 수 있지만 컨텐츠의 읽기 쉽게 유지하는 것은 필수적입니다. 사용자가 단말기에서 텍스트 크기를 변경해도 텍스트가 잘 보이도록 동적 유형을 채택하는 것이 좋습니다. 또한 굵은 글씨와 같은 내게 필요한 옵션에서 내용을 테스트해야 합니다. 자세한 내용은 접근성 및 타이포그래피를 참조하십시오.
>




**Make useful text selectable.** If a text view contains useful information such as an error message, a serial number, or an IP address, consider letting people select and copy it for pasting elsewhere.
> 유용한 텍스트를 선택할 수 있도록 합니다. 텍스트 보기에 오류 메시지, 일련 번호 또는 IP 주소와 같은 유용한 정보가 포함되어 있으면 다른 곳에 붙여넣기 위해 사용자가 선택하고 복사하도록 하십시오.
>




# **Platform considerations**

*No additional considerations for macOS.*

# **iOS, iPadOS**

**Show the appropriate keyboard type.** Several different keyboard types are available, each designed to facilitate a different type of input. To streamline data entry, the keyboard you display when editing a text view should be appropriate for the type of content. For guidance, see [Onscreen keyboards](../components/selection-and-input/onscreen-keyboards).
> 적절한 키보드 유형을 표시합니다. 각각 다른 유형의 입력을 쉽게 하도록 설계된 여러 가지 다른 키보드 유형을 사용할 수 있습니다. 데이터 입력을 간소화하려면 텍스트 보기를 편집할 때 표시되는 키보드가 내용 유형에 적합해야 합니다. 자세한 내용은 화상 키보드를 참조하십시오.
>




# **tvOS**

You can display text in tvOS using a text view. Because text input in tvOS is minimal by design, tvOS uses [text fields](../components/selection-and-input/text-fields) for editable text instead.
> 텍스트 보기를 사용하여 tvOS에서 텍스트를 표시할 수 있습니다. tvOS에서 텍스트 입력은 설계상 최소이기 때문에 편집 가능한 텍스트에 텍스트 필드를 대신 사용합니다.
>




# **watchOS**

You can display text in watchOS either as a label in WatchKit or with a text view in SwiftUI. For guidance, see [Labels](../components/layout-and-organization/labels).
> 시계에 텍스트를 표시할 수 있습니다.WatchKit에서 레이블로 OS를 사용하거나 Swift에서 텍스트 보기를 사용합니다.UI. 자세한 내용은 레이블을 참조하십시오.
>



