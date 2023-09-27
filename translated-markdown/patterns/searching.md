# **[patterns] searching**

# People use various search techniques to find content on their device, within an app, and within a document or file.
> 사람들은 다양한 검색 기술을 사용하여 장치, 앱 내, 문서 또는 파일 내에서 콘텐츠를 찾습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-searching-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-searching-intro-dark_2x.png)

To search for content within an app, people generally expect to use a search bar. When it makes sense, you can personalize the search experience by using what you know about how people interact with your app. For example, you might display recent searches or a search history, or offer search-term suggestions, completions, or corrections based on terms people searched earlier in your app. For guidance, see [Search fields](../components/navigation-and-search/search-fields).
> 앱 내에서 콘텐츠를 검색하기 위해, 사람들은 일반적으로 검색 바를 사용할 것으로 예상한다. 말이 되면 사람들이 앱과 상호 작용하는 방식에 대해 알고 있는 것을 사용하여 검색 환경을 개인화할 수 있습니다. 예를 들어, 최근 검색 또는 검색 기록을 표시하거나 앱에서 이전에 검색한 용어를 기준으로 검색어 제안, 완료 또는 수정을 제공할 수 있습니다. 자세한 내용은 검색 필드를 참조하십시오.
>




In some cases, people appreciate the ability to scope a search or filter the results. For example, people might want to search for items by specifying attributes like creation date, file size, or file type. For guidance, see [Scope bars](https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/search-fields/#scope-bars). You can also help people find content within an open document or file by implementing ways to find content in a window or page in your iOS, iPadOS, or macOS app.
> 어떤 경우에는 검색 범위를 지정하거나 결과를 필터링할 수 있는 기능을 높이 평가하기도 합니다. 예를 들어, 작성 날짜, 파일 크기 또는 파일 형식과 같은 속성을 지정하여 항목을 검색할 수 있습니다. 자세한 내용은 스코프 막대를 참조하십시오. iOS, iPadOS 또는 macOS 앱의 창이나 페이지에서 콘텐츠를 찾는 방법을 구현하여 사람들이 열려 있는 문서나 파일에서 콘텐츠를 찾도록 도울 수도 있습니다.
>




In iOS, iPadOS, and macOS, Spotlight helps people find content across all apps in the system and on the web. When you index and provide information about your app’s content, people can use Spotlight to find content your app contains without opening it first.
> iOS, iPadOS 및 macOS에서 Spotlight는 사람들이 시스템과 웹의 모든 앱에서 콘텐츠를 찾을 수 있도록 도와줍니다. 앱의 콘텐츠에 대한 정보를 인덱싱하고 제공할 때, 사람들은 먼저 열지 않고도 스포트라이트를 사용하여 앱에 포함된 콘텐츠를 찾을 수 있습니다.
>




# **Best practices**

**Make your app’s content searchable.** You can share content with Spotlight by making it indexable and specifying descriptive attributes known as *metadata*. Spotlight extracts, stores, and organizes this information to allow for fast, comprehensive searches.
> 앱의 콘텐츠를 검색할 수 있도록 만듭니다. 인덱싱할 수 있도록 설정하고 메타데이터로 알려진 설명 속성을 지정하여 Spotlight와 콘텐츠를 공유할 수 있습니다. Spotlight는 빠르고 포괄적인 검색을 위해 이 정보를 추출, 저장 및 구성합니다.
>




**Define metadata for custom file types you handle.** Supply a Spotlight File Importer plug-in that describes the types of metadata your file format contains. For developer guidance, see [CSImportExtension](https://developer.apple.com/documentation/corespotlight/csimportextension).
> 처리하는 사용자 지정 파일 형식에 대한 메타데이터를 정의합니다. 파일 형식에 포함된 메타데이터 유형을 설명하는 Spotlight File Importer 플러그인을 제공합니다. 개발자 지침은 CSImport Extension을 참조하십시오.
>




**Use Spotlight to offer advanced file-search capabilities within the context of your app.** For example, you might include a button that instantly initiates a Spotlight search based on the current selection. You might then display a custom view that presents the search results or a filtered subset of them.
> Spotlight를 사용하여 앱의 컨텍스트 내에서 고급 파일 검색 기능을 제공합니다. 예를 들어, 현재 선택한 항목에 따라 Spotlight 검색을 즉시 시작하는 단추를 포함할 수 있습니다. 그런 다음 검색 결과 또는 검색 결과의 필터링된 하위 집합을 표시하는 사용자 정의 보기를 표시할 수 있습니다.
>




**Prefer using the system-provided open and save views.** The system-provided open and save views generally include a built-in search field that people can use to search and filter the entire system. For related guidance, see [File management](../patterns/file-management).
> 시스템에서 제공한 열기 및 저장 보기를 사용합니다. 시스템에서 제공하는 열기 및 저장 보기는 일반적으로 사용자가 전체 시스템을 검색하고 필터링하는 데 사용할 수 있는 기본 제공 검색 필드를 포함합니다. 관련 지침은 파일 관리를 참조하십시오.
>




**Implement a Quick Look generator if your app produces custom file types.** A Quick Look generator helps Spotlight and other apps show previews of your documents. For developer guidance, see [Quick Look](https://developer.apple.com/documentation/quicklook/).
> 앱이 사용자 지정 파일 형식을 생성하는 경우 Quick Look 생성기를 구현합니다. Quick Look 생성기는 Spotlight 및 다른 앱에서 문서 미리 보기를 표시하는 데 도움이 됩니다. 개발자 지침은 빠른 보기를 참조하십시오.
>




# **Platform considerations**

*No additional considerations for iOS, iPadOS, macOS, tvOS, or watchOS.*
> iOS, iPadOS, macOS, tvOS 또는 워치에 대한 추가 고려 사항 없음OS.
>



