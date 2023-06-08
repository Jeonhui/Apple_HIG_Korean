# **[components-navigation-and-search] search-fields**

## A search field lets people search a collection of content for specific terms they enter.
> 검색 필드를 사용하면 입력한 특정 용어에 대한 내용 모음을 검색할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/search-field-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/search-field-intro-dark_2x.png)

A search field is an editable text field that often displays a Search button, a Clear button, and optional placeholder text. Depending on the platform, a search text field can use a token to represent a search term that people enter or an app-defined item that people can use as a filter. A *token* uses a visual treatment that encapsulates the term or item, indicating that people can easily copy or drag the token without having to select the text within it. For an example of a token in macOS, see [Token fields](../components/navigation-and-search/token-fields).
> 검색 필드는 종종 검색 단추, 지우기 단추 및 선택적 자리 표시자 텍스트를 표시하는 편집 가능한 텍스트 필드입니다. 플랫폼에 따라 검색 텍스트 필드는 토큰을 사용하여 사용자가 입력하는 검색어나 사용자가 필터로 사용할 수 있는 앱 정의 항목을 나타낼 수 있습니다. 토큰은 용어나 항목을 캡슐화하는 시각적 처리를 사용하여 사용자가 토큰 내에서 텍스트를 선택하지 않고도 쉽게 토큰을 복사하거나 끌 수 있음을 나타냅니다. macOS의 토큰 예는 토큰 필드를 참조하십시오.
>




# **Best practices**

**Consider providing hints to help guide searching.** For example, Music includes the placeholder text “Artists, Songs, Lyrics, and More” to suggest what people can search for. Avoid using a term like “Search” for placeholder text because it doesn’t provide any helpful information.
> 예를 들어 음악에는 사람들이 검색할 수 있는 항목을 제안하는 자리 표시자 텍스트 "아티스트, 노래, 가사 및 기타"가 포함되어 있습니다. 플레이스홀더 텍스트에는 유용한 정보가 없으므로 "검색"과 같은 용어를 사용하지 마십시오.
>




**Consider providing helpful shortcuts and other content near a search field.** For example, Safari shows bookmarks as soon as people tap or click the search field, letting them select a bookmark to open it immediately. For developer guidance, see [UISearchSuggestion](https://developer.apple.com/documentation/uikit/uisearchsuggestion).
> 예를 들어, Safari는 검색 필드를 누르거나 클릭하는 즉시 책갈피를 표시하여 사용자가 책갈피를 선택하여 즉시 열 수 있도록 합니다. 개발자 지침은 UI 검색 제안을 참조하십시오.
>




**Start the search at an appropriate time.** You can start the search as soon as people start typing, or wait until they choose Return or Enter. Searching while people type provides results that are continuously refined as the text becomes more specific. If the search happens after people finish typing, consider showing a menu while they type that lets them choose from their recent searches or terms you suggest.
> 적절한 시간에 검색을 시작하십시오. 사용자가 입력을 시작하는 즉시 검색을 시작하거나, 반환 또는 입력을 선택할 때까지 기다릴 수 있습니다. 사용자가 입력하는 동안 검색하면 텍스트가 더 구체적으로 지정됨에 따라 지속적으로 세분화되는 결과가 제공됩니다. 사용자가 입력을 마친 후 검색이 수행되면 사용자가 최근 검색 또는 제안한 용어 중에서 선택할 수 있는 메뉴를 표시하는 것이 좋습니다.
>




**Include a Clear button.** People appreciate having a Clear button because it lets them quickly delete their current search terms.
> 지우기 단추를 포함합니다. 사용자는 지우기 단추를 사용하면 현재 검색어를 빠르게 삭제할 수 있기 때문에 이 단추를 사용할 수 있습니다.
>




**Take privacy into consideration before displaying search history.** People might not appreciate having their search history displayed where others might see it. As an alternative, consider offering a scope bar that helps people narrow down results quickly.
> 검색 기록을 표시하기 전에 개인 정보를 고려하십시오. 다른 사용자가 볼 수 있는 위치에 검색 기록을 표시하는 것을 좋아하지 않을 수 있습니다. 다른 방법으로, 사람들이 결과를 빨리 좁힐 수 있도록 도와주는 범위 표시줄을 제공하는 것을 고려해 보십시오.
>




# **Scope bars**

In iOS, iPadOS, and tvOS, you can use a scope bar to help people refine the scope of a search. For developer guidance, see [UISearchBar](https://developer.apple.com/documentation/uikit/uisearchbar).
> iOS, iPadOS 및 tvOS에서 스코프 표시줄을 사용하여 검색 범위를 세분화할 수 있습니다. 개발자 지침은 UI 검색 모음을 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/search-fields/images/scope-bar-ios_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/search-fields/images/scope-bar-ios_2x.png)

**Favor improving search results over including a scope bar.** A scope bar can be useful when there are clearly defined categories for the search, but it’s generally better to improve search results so scoping isn’t necessary.
> 범위 표시줄은 검색에 대해 명확하게 정의된 범주가 있을 때 유용할 수 있지만 일반적으로 범위 지정이 필요하지 않도록 검색 결과를 개선하는 것이 좋습니다.
>




# **Platform considerations**

*Not supported in watchOS.*

# **iOS, iPadOS**

You can display a search field in a navigation bar or within your content area. When you use system-provided components to include a search field in a navigation bar, it automatically receives the appropriate appearance and behaves as people expect. For example, the search bar can hide until people swipe down to reveal it.
> 탐색 모음 또는 내용 영역 내에 검색 필드를 표시할 수 있습니다. 시스템에서 제공한 구성요소를 사용하여 탐색 모음에 검색 필드를 포함하면 자동으로 적절한 모양을 수신하고 사용자가 예상하는 대로 작동합니다. 예를 들어, 검색란은 사람들이 그것을 드러내기 위해 아래로 스와이프할 때까지 숨길 수 있다.
>




**DEVELOPER NOTE**Use [searchController](https://developer.apple.com/documentation/uikit/uinavigationitem/2897305-searchcontroller) if you want to take advantage of the system-provided appearance and behavior of a search field within a navigation bar. If you need to implement custom appearances and behaviors for a search field, consider using [UISearchBar](https://developer.apple.com/documentation/uikit/uisearchbar) to create a field you want to put in a bar or [UISearchTextField](https://developer.apple.com/documentation/uikit/uisearchtextfield/) to apply a custom background to a search field in a content area.
> 개발자 참고 탐색 모음 내 검색 필드의 시스템 제공 모양 및 동작을 활용하려면 searchController를 사용하십시오. 검색 필드에 대해 사용자 정의 모양 및 동작을 구현해야 하는 경우, UISearchBar를 사용하여 막대에 넣을 필드를 만들거나 UISearchTextField를 사용하여 내용 영역의 검색 필드에 사용자 정의 배경을 적용하는 것이 좋습니다.
>




# **macOS**

Although it’s typical to include a search field in a window’s toolbar, you can also display one in the body area.
> 일반적으로 창 도구 모음에 검색 필드를 포함하지만 본문 영역에 검색 필드를 표시할 수도 있습니다.
>




**Avoid supplying an introductory label for a search field within a content area.** People are familiar with the distinctive appearance of a search field, so there is no need to label it. In contrast, when you place a search field in a toolbar, supply the label "Search" so that the label appears when people configure the toolbar to show icons and text or text only.
> 내용 영역 내에서 검색 필드에 대한 소개 레이블을 제공하지 마십시오. 사람들은 검색 필드의 고유한 모양에 익숙하므로 레이블을 지정할 필요가 없습니다. 반대로, 도구 모음에 검색 필드를 배치할 때 "검색" 레이블을 제공하여 사용자가 아이콘과 텍스트 또는 텍스트만 표시하도록 도구 모음을 구성할 때 레이블이 나타나도록 합니다.
>




**Apply the appropriate bezel style to a scope button.** There are two bezel styles you can use. The *recessed* bezel — which makes the button look like it’s slightly inset — is for scope buttons that toggle on and off to narrow focus; the *rounded* bezel is for scope buttons that initiate an action or specify search criteria.
> 스코프 버튼에 적절한 베젤 스타일을 적용합니다. 두 가지 베젤 스타일을 사용할 수 있습니다. 버튼이 약간 삽입된 것처럼 보이는 오목한 베젤은 좁은 초점으로 켜거나 끄는 스코프 버튼을 위한 것이고, 둥근 베젤은 작업을 시작하거나 검색 기준을 지정하는 스코프 버튼을 위한 것입니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/search-fields/images/scope-buttons-macos_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/search-fields/images/scope-buttons-macos_2x.png)

**If appropriate, let people refine the scope.** You can enable supplementary scoping rules using filter rows that appear beneath a scope bar. For example, when searching for a filename in Finder, people can click an Add (+) button to specify additional attributes like an extension or a modification date range. A filter row can include text fields, buttons, and other controls for specifying filter criteria.
> 필요한 경우 사용자가 범위를 세분화하도록 합니다. 범위 표시줄 아래에 나타나는 필터 행을 사용하여 보조 범위 지정 규칙을 사용하도록 설정할 수 있습니다. 예를 들어, Finder에서 파일 이름을 검색할 때 추가(+) 단추를 클릭하여 확장자 또는 수정 날짜 범위와 같은 추가 속성을 지정할 수 있습니다. 필터 행에는 필터 기준을 지정하기 위한 텍스트 필드, 단추 및 기타 컨트롤이 포함될 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/search-fields/images/scope-bar-macos-additional_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/search-fields/images/scope-bar-macos-additional_2x.png)

# **tvOS**

A search screen is a specialized keyboard screen that helps people enter search text, displaying search results beneath the keyboard in a fully customizable view. For developer guidance, see [UISearchController](https://developer.apple.com/documentation/uikit/uisearchcontroller/).
> 검색 화면은 검색 텍스트를 입력하는 데 도움이 되는 특수 키보드 화면으로, 키보드 아래에 검색 결과를 사용자 정의 가능한 보기로 표시합니다. 개발자 지침은 UI 검색 컨트롤러를 참조하십시오.
>




**Consider presenting recent searches.** Because people frequently repeat searches in tvOS, you can minimize the need for text entry by listing popular or recent searches in the results area under the keyboard before people start typing.
> 최근 검색을 표시하는 것을 고려해 보십시오. tvOS에서 검색을 반복하는 경우가 많기 때문에 사용자가 입력을 시작하기 전에 키보드 아래의 결과 영역에 인기 있는 검색이나 최근 검색을 나열하여 텍스트 입력의 필요성을 최소화할 수 있습니다.
>




**Provide suggestions to make searching easier.** People don’t typically want to do a lot of typing in tvOS. To improve the search experience, provide popular and context-specific search suggestions, including recent searches when available. For developer guidance, see [Using suggested searches with a search controller](https://developer.apple.com/documentation/uikit/view_controllers/using_suggested_searches_with_a_search_controller).
> 검색을 쉽게 할 수 있도록 제안을 제공합니다. 사람들은 일반적으로 TVOS에서 많은 타이핑을 하고 싶어하지 않습니다. 검색 환경을 향상시키려면 최근 검색을 포함하여 일반적이고 상황에 맞는 검색 제안을 제공하십시오. 개발자 지침은 검색 컨트롤러와 함께 제안된 검색 사용을 참조하십시오.
>




**Simplify search results.** Avoid providing a lengthy list of search results that requires lots of scrolling. In addition to prioritizing the most likely results, consider categorizing them to help people find what they want.
> 검색 결과를 단순화합니다. 많은 스크롤이 필요한 검색 결과의 긴 목록을 제공하지 마십시오. 가장 가능성이 높은 결과의 우선 순위를 정하는 것 외에도, 사람들이 원하는 결과를 찾는 데 도움이 되도록 결과를 분류하는 것을 고려해 보십시오.
>




**Consider letting people filter search results.** For example, you can include a scope bar in the search results content area to help people quickly and easily filter search results.
> 사용자가 검색 결과를 빠르고 쉽게 필터링할 수 있도록 검색 결과 내용 영역에 범위 표시줄을 포함할 수 있습니다.
>



