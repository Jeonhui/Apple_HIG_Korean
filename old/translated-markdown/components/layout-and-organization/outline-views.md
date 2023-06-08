# **[components-layout-and-organization] outline-views**

## An outline view presents hierarchical data in a scrolling list of cells that are organized into columns and rows.
> 개요 보기는 열과 행으로 구성된 셀 스크롤 목록에 계층 데이터를 표시합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/outline-view-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/outline-view-intro-dark_2x.png)

An outline view includes at least one column that contains primary hierarchical data, such as a set of parent containers and their children. You can add columns, as needed, to display attributes that supplement the primary data; for example, sizes and modification dates. Parent containers have disclosure triangles that expand to reveal their children.
> 개요 보기에는 상위 컨테이너 및 하위 컨테이너 집합과 같은 기본 계층적 데이터가 들어 있는 열이 하나 이상 포함됩니다. 필요에 따라 열을 추가하여 기본 데이터를 보완하는 속성(예: 크기 및 수정 날짜)을 표시할 수 있습니다. 부모 컨테이너에는 자식들을 드러내기 위해 확장되는 노출 삼각형이 있습니다.
>




Finder windows offer an outline view for navigating the file system.
> 파인더 창은 파일 시스템을 탐색하기 위한 개요 보기를 제공합니다.
>




# **Best practices**

Outline views work well to display text-based content and often appear in the leading side of a [split view](../components/layout-and-organization/split-views), with related content on the opposite side.
> 개요 보기는 텍스트 기반 내용을 표시하는 데 적합하며, 종종 분할 보기의 앞쪽에 나타나며, 반대쪽에 관련 내용이 표시됩니다.
>




**Use a table instead of an outline view to present data that’s not hierarchical.** For guidance, see [Lists and tables](../components/layout-and-organization/lists-and-tables).
> 개요 보기 대신 표를 사용하여 계층적이지 않은 데이터를 표시할 수 있습니다. 자세한 내용은 목록 및 표를 참조하십시오.
>




**Expose data hierarchy in the first column only.** Other columns can display attributes that apply to the hierarchical data in the primary column.
> 첫 번째 열에만 데이터 계층 노출. 다른 열에는 기본 열의 계층 데이터에 적용되는 속성이 표시될 수 있습니다.
>




**Use descriptive column headings to provide context.** Use nouns or short noun phrases with [title-style capitalization](https://help.apple.com/applestyleguide/#/apsgb744e4a3?sub=apdca93e113f1d64) and no punctuation; in particular, avoid adding a trailing colon. Always provide column headings in a multi-column outline view. If you don’t include a column heading in a single-column outline view, use a label or other means to make sure there’s enough context.
> 문맥을 제공하려면 설명 열 머리글을 사용하십시오. 제목 형식 대소문자가 있고 구두점이 없는 명사 또는 짧은 명사 구를 사용하십시오. 특히 뒤에 오는 콜론을 추가하지 마십시오. 다중 열 개요 보기에서 항상 열 제목을 제공합니다. 단일 열 개요 보기에 열 제목을 포함하지 않는 경우 레이블 또는 기타 방법을 사용하여 충분한 컨텍스트가 있는지 확인하십시오.
>




**Consider letting people click column headings to sort an outline view.**In a sortable outline view, people can click a column heading to perform an ascending or descending sort based on that column. You can implement additional sorting based on secondary columns behind the scenes, if necessary. If people click the primary column heading, sorting occurs at each hierarchy level. For example, in the Finder, all top-level folders are sorted, then the items within each folder are sorted. If people click the heading of a column that’s already sorted, the folders and their contents are sorted again in the opposite direction.
> 사용자가 열 제목을 눌러 개요 보기를 정렬할 수 있도록 하십시오.정렬 가능한 개요 보기에서 사용자는 열 제목을 눌러 해당 열을 기준으로 오름차순 또는 내림차순 정렬을 수행할 수 있습니다. 필요한 경우 장면 뒤에 있는 보조 열을 기준으로 추가 정렬을 구현할 수 있습니다. 사용자가 기본 열 제목을 누르면 각 계층 수준에서 정렬이 수행됩니다. 예를 들어, 파인더에서 모든 최상위 폴더가 정렬된 다음 각 폴더 내의 항목이 정렬됩니다. 이미 정렬된 열의 제목을 누르면 폴더와 해당 내용이 반대 방향으로 다시 정렬됩니다.
>




**Let people resize columns.** Data displayed in an outline view often varies in width. It’s important to let people adjust column width as needed to reveal data that’s wider than the column.
> 사용자가 열의 크기를 조정할 수 있습니다. 개요 보기에 표시되는 데이터의 너비는 종종 다릅니다. 필요한 경우 사용자가 열 너비를 조정하여 열보다 넓은 데이터를 표시할 수 있도록 하는 것이 중요합니다.
>




**Make it easy for people to expand or collapse nested containers.** For example, clicking a disclosure triangle for a folder in a Finder window expands only that folder. However, Option-clicking the disclosure triangle expands all of its subfolders.
> 예를 들어, 파인더 창에서 폴더에 대한 노출 삼각형을 클릭하면 해당 폴더만 확장됩니다. 그러나 노출 삼각형을 누르면 모든 하위 폴더가 확장됩니다.
>




**Retain people’s expansion choices.** If people expand various levels of an outline view to reach a specific item, store the state so you can display it again the next time. This way, people won’t need to navigate back to the same place again.
> 사용자의 확장 선택사항을 유지합니다. 사용자가 특정 항목에 도달하기 위해 다양한 수준의 아웃라인 보기를 확장한 경우 다음에 다시 표시할 수 있도록 상태를 저장하십시오. 이런 식으로, 사람들은 다시 같은 장소로 돌아갈 필요가 없을 것이다.
>




**Consider using alternating row colors in multi-column outline views.**Alternating colors can make it easier for people to track row values across columns, especially in wide outline views.
> 다중 열 윤곽선 보기에서 행 색상을 번갈아 사용하는 것이 좋습니다.색상을 번갈아 사용하면 특히 넓은 윤곽선 보기에서 사용자가 열 전체에 걸쳐 행 값을 쉽게 추적할 수 있습니다.
>




**Enable data editing if it makes sense in your app.** In an editable outline view cell, people should be able to single-click a cell to edit its contents. Note that a cell can respond differently to a double click. For example, an outline view listing files might let people single-click a file’s name to edit it, but double-click a file’s name to open the file. You can also let people reorder, add, and remove rows if it would be useful.
> 앱에서 데이터 편집이 적절한 경우 데이터 편집을 활성화합니다. 편집 가능한 개요 보기 셀에서 사람들은 셀을 한 번 클릭하여 내용을 편집할 수 있어야 합니다. 셀은 두 번 클릭할 때 다르게 반응할 수 있습니다. 예를 들어 파일을 나열하는 개요 보기를 사용하면 파일 이름을 한 번 눌러 편집할 수 있지만 파일 이름을 두 번 눌러 파일을 열 수 있습니다. 또한 유용한 경우 사용자가 행을 재정렬, 추가 및 제거하도록 할 수 있습니다.
>




**Consider using a centered ellipsis to truncate cell text instead of clipping it.** An ellipsis in the middle preserves the beginning and end of the cell text, which can make the content more distinct and recognizable than clipped text.
> 가운데에 있는 줄임표를 사용하여 셀 텍스트를 자르는 대신 잘라내십시오. 가운데에 있는 줄임표는 셀 텍스트의 시작과 끝을 보존하므로 잘라낸 텍스트보다 내용을 더 명확하게 인식할 수 있습니다.
>




**Consider offering a search field to help people find values quickly in a lengthy outline view.** Windows with an outline view as the primary feature often include a search field in the toolbar. For guidance, see [Search fields](../components/navigation-and-search/search-fields).
> 사용자가 긴 개요 보기에서 값을 빨리 찾을 수 있도록 검색 필드를 제공하는 것이 좋습니다. 개요 보기를 기본 기능으로 사용하는 Windows(윈도우)에는 종종 도구 모음에 검색 필드가 포함됩니다. 자세한 내용은 검색 필드를 참조하십시오.
>




# **Platform considerations**

*Not supported in iOS, iPadOS, tvOS, or watchOS.*
> iOS, iPadOS, tvOS 또는 시계에서 지원되지 않음OS.
>



