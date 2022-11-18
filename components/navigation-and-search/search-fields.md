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




