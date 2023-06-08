# **[components-layout-and-organization] list-and-tables**

## Lists and tables present data in one or more columns of rows.
> 목록과 표는 하나 이상의 행 열에 데이터를 표시합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/lists-and-tables-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/lists-and-tables-intro-dark_2x.png)

A table or list can represent data that’s organized in groups or hierarchies, and it can enable user interactions like selecting, adding, deleting, and reordering. Apps and games in all platforms can use tables to present content and options; many apps use lists to express an overall information hierarchy and enable navigation. For example, iOS Settings uses a hierarchy of lists to help people choose options, and several apps — such as Mail in iPadOS and macOS — use a table within a [split view](../components/layout-and-organization/split-views).
> 테이블 또는 목록은 그룹 또는 계층으로 구성된 데이터를 나타낼 수 있으며, 선택, 추가, 삭제 및 정렬과 같은 사용자 상호 작용을 활성화할 수 있습니다. 모든 플랫폼의 앱과 게임은 테이블을 사용하여 콘텐츠와 옵션을 표시할 수 있습니다. 많은 앱은 목록을 사용하여 전체 정보 계층을 표현하고 탐색을 활성화합니다. 예를 들어 iOS 설정에서는 목록 계층을 사용하여 사용자가 옵션을 선택할 수 있도록 돕고, iPadOS 및 macOS의 메일과 같은 여러 앱은 분할 보기 내의 테이블을 사용합니다.
>




Sometimes, people need to work with complex data in a multicolumn table or a spreadsheet. Apps that enable productivity tasks often use a table to represent various characteristics or attributes of the data in separate, sortable columns.
> 때때로 사람들은 다중 열 테이블이나 스프레드시트의 복잡한 데이터로 작업해야 한다. 생산성 작업을 가능하게 하는 앱은 종종 표를 사용하여 데이터의 다양한 특성이나 속성을 별도의 정렬 가능한 열로 표현한다.
>




# **Best practices**

**Prefer displaying text in a list or table.** A table can include any type of content, but the row-based format is especially well suited to making text easy to scan and read. If you have items that vary widely in size — or you need to display a large number of images — consider using a [collection](../components/layout-and-organization/collections)instead.
> 목록이나 테이블에 텍스트를 표시하는 것을 선호합니다. 테이블에는 모든 유형의 내용이 포함될 수 있지만 행 기반 형식은 텍스트를 스캔하고 읽기 쉽게 만드는 데 특히 적합합니다. 크기가 매우 다양한 항목이 있거나 많은 수의 이미지를 표시해야 하는 경우 대신 컬렉션을 사용하는 것이 좋습니다.
>




**Let people edit a table when it makes sense.** People appreciate being able to reorder a list, even if they can’t add or remove items. In iOS and iPadOS, people must enter an edit mode before they can select table items.
> 사람들은 항목을 추가하거나 제거할 수 없는 경우에도 목록을 다시 정렬할 수 있는 것을 높이 평가합니다. iOS와 iPadOS에서는 테이블 항목을 선택하기 전에 편집 모드에 들어가야 합니다.
>




**Provide appropriate feedback when people select a list item.** The feedback can vary depending on whether selecting the item reveals a new view or toggles the item’s state. In general, a table that enables navigation through a hierarchy persistently highlights the selected row to clarify the path people are taking. In contrast, a table that lists options often highlights a row only briefly before adding an image — such as a checkmark — indicating that the item is selected.
> 사용자가 목록 항목을 선택할 때 적절한 피드백을 제공하십시오. 항목을 선택하면 새 보기가 나타나는지 또는 항목 상태를 전환하는지 여부에 따라 피드백이 달라질 수 있습니다. 일반적으로 계층을 통해 탐색할 수 있는 테이블은 선택한 행을 지속적으로 강조 표시하여 사람들이 가는 경로를 명확히 합니다. 이와 대조적으로 옵션을 나열하는 테이블은 종종 항목이 선택되었음을 나타내는 체크 표시와 같은 이미지를 추가하기 전에 행을 짧게 강조 표시합니다.
>




# **Content**

**Keep item text succinct so row content is comfortable to read.** Short, succinct text can help minimize truncation and wrapping, making text easier to read and scan. If each item consists of a large amount of text, consider alternatives that help you avoid displaying over-large table rows. For example, you could list item titles only, letting people choose an item to reveal its content in a detail view.
> 행 내용이 읽기 쉽도록 항목 텍스트 간결함을 유지합니다. 짧고 간결한 텍스트는 잘라내기 및 래핑을 최소화하여 텍스트를 읽고 스캔하기 쉽게 합니다. 각 항목이 많은 양의 텍스트로 구성된 경우 너무 큰 테이블 행을 표시하지 않도록 하는 데 도움이 되는 대안을 고려하십시오. 예를 들어, 항목 제목만 나열하여 사용자가 세부 보기에 내용을 표시할 항목을 선택할 수 있습니다.
>




**Consider ways to preserve readability of text that might otherwise get clipped or truncated.** When a table is narrow — for example, if people can vary its width — you want content to remain recognizable and easy to read. Sometimes, an ellipsis in the middle of text can make an item easier to distinguish because it preserves both the beginning and the end of the content.
> 테이블이 좁을 때(예: 사용자가 너비를 변경할 수 있는 경우) 내용을 인식 가능하고 읽기 쉽게 유지하기를 원하는 경우, 텍스트의 가독성을 유지하는 방법을 고려하십시오. 텍스트 중간에 줄임표를 사용하면 내용의 시작과 끝을 모두 보존하기 때문에 항목을 쉽게 구분할 수 있습니다.
>




**Use descriptive column headings in a multicolumn table.** Use nouns or short noun phrases with title-style capitalization, and don’t add ending punctuation. If you don’t include a column heading in a single-column table view, use a label or a header to help people understand the context.
> 다중 열 표에 설명 열 제목을 사용합니다. 제목 형식 대소문자를 사용하는 명사 또는 짧은 명사 구문을 사용하고 끝 구두점을 추가하지 마십시오. 단일 열 표 보기에 열 제목을 포함하지 않는 경우, 레이블 또는 헤더를 사용하여 사용자가 컨텍스트를 이해하는 데 도움이 됩니다.
>




# **Style**

**Choose a table or list style that coordinates with your data and platform.** Some styles use visual details to help communicate grouping and hierarchy or to enable specific experiences. In iOS and iPadOS, for example, the grouped style uses headers, footers, and additional space to separate groups of data; the elliptical style available in watchOS makes items appear is if they’re rolling off a rounded surface as people scroll; and macOS defines a bordered style that uses alternating row backgrounds to help make large tables easier to use. For developer guidance, see [ListStyle](https://developer.apple.com/documentation/swiftui/liststyle).
> 데이터 및 플랫폼에 맞게 조정되는 테이블 또는 목록 스타일을 선택하십시오. 일부 스타일에서는 그룹 및 계층 구조를 전달하거나 특정 경험을 활성화하기 위해 시각적 세부 정보를 사용합니다. 예를 들어 iOS와 iPadOS에서 그룹화된 스타일은 헤더, 바닥글 및 추가 공간을 사용하여 데이터 그룹을 분리합니다. 시계에서 사용할 수 있는 타원형 스타일OS는 사용자가 스크롤할 때 둥근 표면에서 굴러떨어지는 경우로, macOS는 큰 테이블을 쉽게 사용할 수 있도록 행 배경을 번갈아 사용하는 경계 스타일을 정의합니다. 개발자 지침은 ListStyle을 참조하십시오.
>




**Choose a row style that fits the information you need to display.** For example, you might need to display a small image in the leading end of a row, followed by a brief explanatory label. Some platforms provide built-in row styles you can use to arrange content in list rows, such as the [UIListContentConfiguration](https://developer.apple.com/documentation/uikit/uilistcontentconfiguration) API you can use to lay out content in a list’s rows, headers, and footers in iOS, iPadOS, and tvOS.
> 표시해야 하는 정보에 맞는 행 스타일을 선택하십시오. 예를 들어, 행의 맨 앞에 작은 이미지를 표시한 다음 간단한 설명 레이블을 표시해야 할 수 있습니다. 일부 플랫폼은 iOS, iPadOS 및 tvOS에서 목록의 행, 머리글 및 바닥글에 내용을 레이아웃하는 데 사용할 수 있는 UIlistContentConfiguration API와 같이 목록 행에 내용을 정렬하는 데 사용할 수 있는 기본 제공 행 스타일을 제공합니다.
>




# **Platform considerations**

# **iOS, iPadOS**

**Use an info button only to reveal more information about a row’s content.** An info button — called a *detail disclosure button* when it appears in a list row — doesn’t enable navigation through a hierarchical table or list. If you need to let people drill into a list or table row’s subviews, use a disclosure indicator accessory control. For developer guidance, see [disclosureIndicator](https://developer.apple.com/documentation/uikit/uitableviewcell/accessorytype/disclosureindicator).
> 행의 내용에 대한 자세한 정보를 표시하려면 정보 단추만 사용하십시오. 목록 행에 세부 정보 노출 단추라고 하는 정보 단추는 계층 테이블이나 목록을 탐색할 수 없습니다. 사용자가 목록 또는 테이블 행의 하위 보기를 드릴로 뚫도록 해야 하는 경우 노출 표시기 보조 컨트롤을 사용하십시오. 개발자 지침은 공개를 참조하십시오.표시기.
>




![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/lists-and-tables/images/info-button-in-list_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/lists-and-tables/images/info-button-in-list_2x.png)

An info button shows details about a list item; it doesn’t enable navigation.
> 정보 단추는 목록 항목에 대한 세부 정보를 표시하며 탐색을 활성화하지 않습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/lists-and-tables/images/disclosure-indicator-in-list_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/lists-and-tables/images/disclosure-indicator-in-list_2x.png)

A disclosure indicator reveals the next level in a hierarchy; it doesn’t show details about the item.
> 노출 표시기는 계층의 다음 수준을 표시하며 항목에 대한 세부 정보를 표시하지 않습니다.
>




**Avoid adding an index to a table that displays controls — like disclosure indicators — in the trailing ends of its rows.** An *index* typically consists of the letters in an alphabet, displayed vertically at the trailing side of a list. People can jump to a specific section in the list by choosing the index letter that maps to it. Because both the index and elements like disclosure indicators appear on the trailing side of a list, it can be difficult for people to use one element without activating the other.
> 노출 표시기와 같은 컨트롤을 행의 후미에 표시하는 테이블에 인덱스를 추가하지 마십시오. 인덱스는 일반적으로 목록의 후미에 수직으로 표시되는 알파벳 문자로 구성됩니다. 사용자는 목록에 매핑되는 색인 문자를 선택하여 목록의 특정 섹션으로 이동할 수 있습니다. 지수 및 공시 지표와 같은 요소는 모두 목록의 뒷면에 나타나기 때문에, 사람들이 다른 요소를 활성화하지 않고 한 요소를 사용하는 것은 어려울 수 있다.
>




# **macOS**

**When it provides value, let people click a column heading to sort a table view based on that column**. If people click the heading of a column that’s already sorted, re-sort the data in the opposite direction.
> 값을 제공하는 경우 사용자가 열 제목을 눌러 해당 열을 기준으로 테이블 보기를 정렬할 수 있습니다. 이미 정렬된 열의 제목을 클릭하면 데이터가 반대 방향으로 다시 정렬됩니다.
>




**Let people resize columns.** Data displayed in a table view often varies in width. People appreciate resizing columns to help them focus on different areas or reveal clipped data.
> 사용자가 열의 크기를 조정할 수 있도록 합니다. 표 보기에 표시되는 데이터의 너비는 종종 다릅니다. 사람들은 다른 영역에 초점을 맞추거나 잘린 데이터를 표시하기 위해 열의 크기를 조정하는 것을 높이 평가한다.
>




**Consider using alternating row colors in a multicolumn table.**Alternating colors can help people track row values across columns, especially in a wide table.
> 다중 열 표에 행 색상을 번갈아 사용하는 것이 좋습니다.색상을 번갈아 사용하면 특히 넓은 테이블에서 열에서 행 값을 추적할 수 있습니다.
>




**Use an outline view instead of a table view to present hierarchical data.**An [outline view](../components/layout-and-organization/outline-views) looks like a table view, but includes disclosure triangles for exposing nested levels of data. For example, an outline view might display folders and the items they contain.
> 테이블 보기 대신 아웃라인 보기를 사용하여 계층 데이터를 표시할 수 있습니다.개요 보기는 테이블 보기처럼 보이지만 중첩된 데이터 수준을 노출하기 위한 노출 삼각형이 포함되어 있습니다. 예를 들어 아웃라인 보기에 폴더와 폴더에 포함된 항목이 표시될 수 있습니다.
>




# **tvOS**

**Confirm that images near a table still look good as each row highlights and slightly increases in size when it becomes focused.** A focused row’s corners can also become rounded, which may affect the appearance of images on either side of it. Account for this effect as you prepare images, and don’t add your own masks to round the corners.
> 각 행이 강조되고 초점이 맞춰질 때 크기가 약간 증가해도 테이블 근처의 이미지가 여전히 좋아 보이는지 확인합니다. 포커싱된 행의 모서리가 둥글어질 수도 있으며, 이는 표의 양쪽에 있는 이미지의 모양에 영향을 줄 수 있습니다. 이미지를 준비할 때 이 효과를 설명하고 모서리를 둥글게 만들기 위해 마스크를 추가하지 마십시오.
>




# **watchOS**

**When possible, limit the number of rows.** Short lists are easier for people to scan, but sometimes people expect a long list of items. For example, if people subscribe to a large number of podcasts, they might think something's wrong if they can't view all their items. You can help make a long list more manageable by listing the most relevant items and providing a way for people to view more.
> 가능한 경우 행 수를 제한하십시오. 짧은 목록을 검색하는 것이 더 쉽지만 긴 항목 목록이 필요한 경우도 있습니다. 예를 들어, 만약 사람들이 많은 수의 팟캐스트를 구독한다면, 그들은 만약 그들이 그들의 모든 항목을 볼 수 없다면, 그들은 무언가 잘못되었다고 생각할지도 모른다. 가장 관련성이 높은 항목을 나열하고 사람들이 더 많이 볼 수 있는 방법을 제공함으로써 긴 목록을 보다 쉽게 관리할 수 있도록 도울 수 있습니다.
>




**Constrain the length of detail views if you want to support vertical page-based navigation.** People use vertical page-based navigation to swipe vertically among the detail items of different list rows. Navigating in this way saves time because people don't need to return to the list to tap a new detail item, but it works only when detail views are short. If your detail views scroll, people won't be able to use vertical page-based navigation to swipe among them.
> 세로 페이지 기반 탐색을 지원하려면 상세 보기의 길이를 제한하십시오. 사용자는 세로 페이지 기반 탐색을 사용하여 서로 다른 목록 행의 상세 항목 사이에서 세로로 스와이프합니다. 이러한 방식으로 탐색하면 사용자가 새 세부 항목을 누르기 위해 목록으로 돌아갈 필요가 없으므로 시간이 절약되지만 세부 보기가 짧을 때만 작동합니다. 세부 보기가 스크롤되면, 사람들은 세로 페이지 기반 탐색을 사용하여 세부 보기 사이를 이동할 수 없습니다.
>



