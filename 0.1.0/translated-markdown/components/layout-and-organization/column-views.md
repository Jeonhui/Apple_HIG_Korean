# **[components-layout-and-organization] column-views**

## A column view — also called a *browser* — lets people view and navigate a data hierarchy using a series of vertical columns.
> 열 보기(브라우저라고도 함)를 사용하여 일련의 세로 열을 사용하여 데이터 계층을 보고 탐색할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/column-view-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/column-view-intro-dark_2x.png)

Each column represents one level of the hierarchy and contains horizontal rows of data items. Within a column, any parent item that contains nested child items is marked with a triangle icon. When people select a parent, the next column displays its children. People can continue navigating in this way until they reach an item with no children, and can also navigate back up the hierarchy to explore other branches of data.
> 각 열은 계층의 한 수준을 나타내며 데이터 항목의 수평 행을 포함합니다. 열 내에서 중첩된 하위 항목을 포함하는 상위 항목은 삼각형 아이콘으로 표시됩니다. 사용자가 부모를 선택하면 다음 열에 해당 자녀가 표시됩니다. 사용자는 자녀가 없는 항목에 도달할 때까지 이러한 방식으로 탐색을 계속할 수 있으며, 계층 위로 다시 탐색하여 다른 데이터 지점을 탐색할 수도 있습니다.
>




# **Best practices**

Consider using a column view when you have a deep data hierarchy in which people tend to navigate back and forth frequently between levels, and you don’t need the sorting capabilities that a [list or table](../components/layout-and-organization/lists-and-tables) provides. For example, Finder offers a column view (in addition to icon, list, and gallery views) for navigating directory structures.
> 사용자가 수준 간에 자주 왔다 갔다 하는 경향이 있고 목록이나 테이블이 제공하는 정렬 기능이 필요하지 않은 경우 열 보기를 사용하는 것이 좋습니다. 예를 들어, Finder는 디렉토리 구조를 탐색하기 위한 열 보기(아이콘, 목록 및 갤러리 보기 외에도)를 제공합니다.
>




**Show the root level of your data hierarchy in the first column.** People know they can quickly scroll back to the first column to begin navigating the hierarchy from the top again.
> 첫 번째 열에 데이터 계층의 루트 수준을 표시합니다. 사람들은 그들이 첫 번째 열로 빠르게 스크롤하여 위로부터 계층 구조를 다시 탐색할 수 있다는 것을 알고 있습니다.
>




**Consider showing information about the selected item when there are no nested items to display.** The Finder, for example, shows a preview of the selected item and information like the creation date, modification date, file type, and size.
> 표시할 중첩 항목이 없는 경우 선택한 항목에 대한 정보를 표시하는 것이 좋습니다. 예를 들어, 파인더는 선택한 항목의 미리 보기와 작성 날짜, 수정 날짜, 파일 형식 및 크기와 같은 정보를 표시합니다.
>




**Let people resize columns.** This is especially important if the names of some data items are too long to fit within the default column width.
> 사용자가 열의 크기를 조정할 수 있도록 합니다. 일부 데이터 항목의 이름이 너무 길어서 기본 열 너비에 맞지 않을 경우 특히 중요합니다.
>




# **Platform considerations**

*Not supported in iOS, iPadOS, tvOS, or watchOS.*
> iOS, iPadOS, tvOS 또는 시계에서 지원되지 않음OS.
>




# **iPadOS**

If you need to manage the presentation of hierarchical content in iPadOS, consider using a [split view](../components/layout-and-organization/split-views).
> iPadOS에서 계층적 콘텐츠의 프레젠테이션을 관리해야 하는 경우 분할 보기를 사용하는 것을 고려해 보십시오.
>



