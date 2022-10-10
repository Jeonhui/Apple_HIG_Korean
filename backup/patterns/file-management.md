# **[patterns] file-management**

# Depending on the experience, people may expect to manage their documents and files within an app or throughout the system.
> 경험에 따라 사람들은 앱 내에서 또는 시스템 전체에서 문서와 파일을 관리할 것으로 기대할 수 있다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-file-management-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-file-management-intro-dark_2x.png)

Document-based apps — such as Pages, Keynote, Photos, Notes, Sketch, and Adobe Illustrator — help people create, edit, and save documents and files, often providing customized ways for people to browse for content they want to open in the app.
> 페이지, 키노트, 사진, 노트, 스케치 및 Adobe Illustrator와 같은 문서 기반 앱은 사용자가 문서 및 파일을 만들고 편집하고 저장하는 데 도움이 되며, 사용자가 앱에서 열고자 하는 콘텐츠를 탐색할 수 있는 사용자 지정 방법을 종종 제공합니다.
>




Depending on the platform, people may also expect to browse files without first opening an app. On a Mac, people use the Finder to access the macOS file system; on iPhone and iPad, people use the Files app to manage the documents and files on their device. In watchOS and tvOS, people don’t typically create, edit, and manage documents.
> 플랫폼에 따라, 사람들은 앱을 열지 않고도 파일을 탐색할 것으로 예상할 수 있다. Mac에서는 Finder를 사용하여 MacOS 파일 시스템에 액세스하고 iPhone 및 iPad에서는 Files 앱을 사용하여 단말기의 문서와 파일을 관리합니다. watchOS와 tvOS에서는 일반적으로 문서를 작성, 편집 및 관리하지 않습니다.
>




# **Opening files**

People are familiar with the system apps and interfaces for browsing and opening files, so it can work well to leverage these experiences in your app.
> 사람들은 파일을 검색하고 열기 위한 시스템 앱과 인터페이스에 익숙하므로 앱에서 이러한 경험을 잘 활용할 수 있습니다.
>




**Use app menus and keyboard shortcuts to give people convenient ways to create and open documents.** In macOS and iPadOS, people expect to create new documents or open existing ones by using commands in an app-level File menu. When you enable menu commands like New or Open..., macOS presents them in the menu bar File menu, and iPadOS presents them in the shortcuts interface that displays when people hold the Command key on a connected hardware keyboard. iOS doesn’t display app-level menus in these ways, so it often works well to use an Add (+) button to enable a “new document” action.
> 앱 메뉴와 바로 가기 키를 사용하여 사람들에게 문서를 만들고 열 수 있는 편리한 방법을 제공하십시오. macOS와 iPadOS에서 사람들은 앱 수준의 파일 메뉴에서 명령을 사용하여 새로운 문서를 만들거나 기존 문서를 열기를 기대합니다. 새로 만들기 또는 열기...와 같은 메뉴 명령을 활성화하면 macOS는 메뉴 바 파일 메뉴에 표시되며 iPadOS는 연결된 하드웨어 키보드에서 명령 키를 누르면 표시되는 바로 가기 인터페이스에 표시됩니다. iOS는 이러한 방식으로 앱 수준 메뉴를 표시하지 않으므로 "새로 만들기"를 활성화하기 위해 추가(+) 버튼을 사용하는 것이 잘 작동하는 경우가 많습니다.문서" 작업을 수행합니다.
>




**Reflect people’s view of the file system within a custom file-opening interface.** Through their use of the Finder and Files, people understand the basic layout of their device’s file system, so it’s a good idea to build on this understanding in a custom file-opening view. Although it can make sense to start by showing one part of the file system within your custom interface — such as a Documents or iCloud folder, or the most recently selected location — avoid forcing people to remain within this area if they want to browse elsewhere.
> 사용자 지정 파일 열기 인터페이스에 파일 시스템에 대한 사용자의 견해를 반영합니다. 파인더 및 파일 사용을 통해 사용자는 장치 파일 시스템의 기본 레이아웃을 이해하므로 사용자 지정 파일 열기 보기에서 이 이해를 기반으로 하는 것이 좋습니다. 사용자 지정 인터페이스(예: Documents 또는 iCloud 폴더 또는 가장 최근에 선택한 위치) 내에서 파일 시스템의 한 부분을 표시하는 것으로 시작하는 것이 타당할 수 있지만, 다른 곳에서 찾아보기를 원하는 경우 사용자가 이 영역 내에 머무르도록 강제하는 것은 피해야 합니다.
>




**Consider ways to make your custom file-opening interface more convenient.** For example, people might appreciate an “open recent” action in addition to the simple “open” action. You might also want to let people choose criteria on which to filter the file-browsing experience, or select multiple documents to open at once. In a macOS open panel, you can customize the title of the Open button to reflect the task — for example, if your app lets people insert a file’s contents into the current document, you might change the title to *Insert*.
> 사용자 지정 파일 열기 인터페이스를 보다 편리하게 만드는 방법을 고려하십시오. 예를 들어, 사람들은 단순한 "개방" 조치 외에 "개방된 최근" 조치를 평가할 수 있다. 또한 사용자가 파일 검색 환경을 필터링할 기준을 선택하거나 동시에 열 여러 문서를 선택할 수도 있습니다. MacOS 열린 패널에서 작업을 반영하도록 열기 단추의 제목을 사용자 지정할 수 있습니다. 예를 들어, 프로그램에서 현재 문서에 파일 내용을 삽입할 수 있는 경우 제목을 삽입으로 변경할 수 있습니다.
>




# **Saving work**

**Help people be confident that their work is always preserved unless they cancel or delete it.** In general, avoid making people take an explicit action to save their work. Instead, automatically perform periodic saves while they’re editing and when they close a file or switch to another app.
> 작업을 취소하거나 삭제하지 않는 한 작업 내용이 항상 보존된다는 확신을 가질 수 있습니다. 일반적으로, 사람들이 작업을 저장하기 위해 명시적인 조치를 취하도록 하는 것을 피하십시오. 대신 편집하는 동안 또는 파일을 닫거나 다른 앱으로 전환할 때 정기적으로 자동으로 저장을 수행합니다.
>




**Provide a save interface to let people change a file’s name, format, or location.** By default, a new document’s title is “Untitled” until people choose a custom name. As with a document-opening interface, a save view can also enable a browsing experience that defaults to a logical location to help people place the saved document where they want. If you support saving content in different formats, also enable a way for people to choose a specific file format.
> 파일 이름, 형식 또는 위치를 변경할 수 있는 저장 인터페이스를 제공합니다. 기본적으로, 사용자가 사용자 정의 이름을 선택할 때까지 새 문서의 제목은 "제목 없음"입니다. 문서 열기 인터페이스와 마찬가지로, 저장 보기는 또한 사람들이 저장된 문서를 원하는 위치에 배치하는 데 도움이 되는 논리적 위치로 기본 설정되는 검색 환경을 가능하게 할 수 있습니다. 다른 형식으로 내용 저장을 지원하는 경우, 사용자가 특정 파일 형식을 선택할 수도 있습니다.
>




**Hide the file extension by default, but let people view it if they choose.** Be sure to reflect the current choice in all the save or open interfaces you display.
> 기본적으로 파일 확장명을 숨기지만 사용자가 선택한 경우 파일 확장명을 볼 수 있습니다. 표시되는 모든 저장 또는 열린 인터페이스에 현재 선택한 내용을 반영해야 합니다.
>




**Extend the functionality of the Save dialog, if appropriate.** If it makes sense in your app, you can add a custom accessory view containing useful settings or options to the Save dialog. For example, the dialog for saving Mail messages as files contains an option to include attachments.
> 적절한 경우 저장 대화 상자의 기능을 확장합니다. 앱에서 사용할 수 있는 경우 유용한 설정이나 옵션이 포함된 사용자 지정 액세서리 보기를 저장 대화 상자에 추가할 수 있습니다. 예를 들어, 메일 메시지를 파일로 저장하기 위한 대화상자에는 첨부 파일을 포함하는 선택사항이 있습니다.
>




# **Quick Look previews**

Quick Look helps you create previews of the files your app handles so that people can view them within your app and in some cases interact with them. On a Mac, for example, people can play the preview of an audio file; in iOS, people can add markup to a photo’s preview.
> Quick Look을 사용하면 앱에서 처리하는 파일의 미리보기를 만들 수 있으므로 사용자가 앱 내에서 파일을 볼 수 있고 경우에 따라서는 파일과 상호 작용할 수 있습니다. 예를 들어 맥에서는 오디오 파일의 미리 보기를 재생할 수 있으며 iOS에서는 사진 미리보기에 마크업을 추가할 수 있습니다.
>




**Implement a Quick Look viewer in your app if it makes sense.** If your app lets people attach or otherwise interact with files — especially files your app doesn’t natively support — implementing a Quick Look viewer lets people preview those files without leaving your app.
> 이치에 맞으면 앱에 빠른 보기 뷰어를 구현합니다. 앱에서 사용자가 파일을 첨부하거나 다른 방식으로 상호 작용할 수 있는 경우(특히 앱에서 기본적으로 지원하지 않는 파일) 빠른 보기 뷰어를 구현하면 앱을 종료하지 않고도 해당 파일을 미리 볼 수 있습니다.
>




**Consider implementing a Quick Look generator if your app produces custom file types.** A Quick Look generator lets other apps — including Finder, Files, and Spotlight — display previews of your documents, making it easier for people to find them.
> 앱에서 사용자 지정 파일 형식을 생성하는 경우 Quick Look 생성기를 구현하는 것을 고려하십시오. 빠른 보기 생성기를 사용하면 파인더, 파일 및 스포트라이트를 비롯한 다른 앱에서 문서를 미리 볼 수 있으므로 사용자가 문서를 쉽게 찾을 수 있습니다.
>




# **Platform considerations**

*No additional considerations for tvOS or watchOS.*
> tvOS 또는 시청에 대한 추가 고려 사항 없음OS.
>




# **iOS, iPadOS**

If it makes sense for your app to share its files with other apps, you can create a file provider app extension that displays a custom interface for importing, exporting, opening, and moving your app’s documents. For developer guidance, see [File Provider](https://developer.apple.com/documentation/fileprovider). An *app extension* is code you provide that people can install and use to extend the functionality of a specific area of the system; to learn more, see [App extensions](https://developer.apple.com/app-extensions/).
> 앱이 다른 앱과 파일을 공유하는 것이 타당하다면 앱의 문서를 가져오고, 내보내고, 열고, 이동하기 위한 사용자 지정 인터페이스를 표시하는 파일 공급자 앱 확장을 만들 수 있습니다. 개발자 지침은 파일 공급자를 참조하십시오. 앱 확장자는 사용자가 시스템의 특정 영역의 기능을 확장하기 위해 설치하고 사용할 수 있는 코드입니다. 자세한 내용은 앱 확장을 참조하십시오.
>




**When someone uses your file provider extension to open or import documents, display only documents that are appropriate in the current context.** For example, if a PDF-editing app loads your extension, only list PDF files for opening or import. You might also want to display additional information, such as modification dates, sizes, and whether documents are local or remote.
> 파일 공급자 확장명을 사용하여 문서를 열거나 가져올 때 현재 컨텍스트에 적합한 문서만 표시합니다. 예를 들어 PDF 편집 앱이 확장자를 로드하는 경우 열거나 가져올 PDF 파일만 나열합니다. 수정 날짜, 크기, 문서가 로컬인지 원격인지와 같은 추가 정보를 표시할 수도 있습니다.
>




**Let people select a destination when exporting and moving documents.** Unless your app stores documents in a single directory, let people navigate to a specific destination in your directory hierarchy. If it makes sense, you can also provide a way to add new subdirectories.
> 문서를 가져가거나 이동할 때 사용자가 대상을 선택할 수 있습니다. 응용프로그램이 단일 디렉토리에 문서를 저장하지 않는 한, 사용자가 디렉토리 계층의 특정 대상으로 이동할 수 있도록 합니다. 이 경우 새 하위 디렉터리를 추가하는 방법도 제공할 수 있습니다.
>




**Avoid including a custom navigation bar.** Your extension loads within a modal view that already includes a navigation bar. Providing a second navigation bar is confusing and takes space away from your content.
> 사용자 정의 탐색 모음을 포함하지 않도록 합니다. 확장명은 탐색 막대가 이미 포함된 모달 보기 내에 로드됩니다. 두 번째 탐색 모음을 제공하면 내용이 혼란스럽고 공간이 줄어듭니다.
>




Your app can also let people browse and open files from other apps. For developer guidance, see [Adding a document browser to your app](https://developer.apple.com/documentation/uikit/view_controllers/adding_a_document_browser_to_your_app).
> 또한 다른 앱에서 파일을 탐색하고 열 수 있습니다. 개발자 지침은 앱에 문서 브라우저 추가를 참조하십시오.
>




# **macOS**

### **Finder Sync extensions**

If your app syncs local and remote files, you can create a Finder Sync app extension to express file synchronization status and control within the Finder. For developer guidance, see [Finder Sync](https://developer.apple.com/documentation/findersync).
> 앱이 로컬 및 원격 파일을 동기화하는 경우 파인더 동기화 앱 확장을 만들어 파인더 내에서 파일 동기화 상태 및 제어를 표현할 수 있습니다. 개발자 지침은 파인더 동기화를 참조하십시오.
>




For example, you can use a Finder Sync extension to:
> 예를 들어 Finder Sync 확장을 사용하여 다음을 수행할 수 있습니다.
>




- Display badges in the Finder to indicate the sync status of items
- >  파인더에 배지를 표시하여 항목의 동기화 상태를 나타냅니다.

- Provide custom contextual menu items that perform file and folder management tasks, like favoriting and adding password-protection
- >  암호 보호 즐겨찾기 및 추가와 같은 파일 및 폴더 관리 작업을 수행하는 사용자 지정 상황별 메뉴 항목 제공

- Provide custom toolbar buttons that perform global actions, like initiating a sync operation
- >  동기화 작업 시작과 같은 전역 작업을 수행하는 사용자 지정 도구 모음 단추 제공


**Help people avoid losing work if they turn off autosaving.** People can turn off autosaving by selecting the “Ask to keep changes when closing documents” checkbox in the General system settings pane. In this scenario, show that a document has unsaved changes and present a save dialog when people choose to close the document, quit your app, log out, or restart.
> 사람들이 자동 절약을 끄면 실직하지 않도록 도와줍니다. 일반 시스템 설정 영역에서 "문서 닫기 시 변경사항 보관 요청" 확인란을 선택하여 자동 저장을 해제할 수 있습니다. 이 시나리오에서는 문서에 저장되지 않은 변경사항이 있음을 보여주고 사용자가 문서를 닫거나 앱을 종료하거나 로그아웃하거나 다시 시작하도록 선택할 때 저장 대화 상자를 표시합니다.
>




