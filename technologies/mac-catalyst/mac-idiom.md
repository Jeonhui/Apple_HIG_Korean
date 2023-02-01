# **[technologies-mac-catalyst] mac-idiom**

When you first create your Mac app with Mac Catalyst, Xcode defaults to the iPad idiom. With this setting, the system ensures that your Mac app appears consistent with the macOS display environment without requiring significant changes to the app’s layout. However, text and graphics may appear slightly less detailed.
> Mac Catalyst로 Mac 앱을 처음 만들 때 Xcode는 기본적으로 iPad 관용구로 설정됩니다. 이 설정을 사용하면 Mac 앱의 레이아웃을 크게 변경할 필요 없이 Mac 앱이 MacOS 디스플레이 환경과 일관되게 표시됩니다. 그러나 텍스트와 그래픽은 약간 덜 상세하게 나타날 수 있습니다.
>




After you’ve spent time making your app feel at home on the Mac, consider switching to the Mac idiom. With this setting, text and artwork renders in more detail, and some interface elements and views take on an even more Mac-like appearance.
> Mac에서 앱이 집에 있는 것처럼 느껴지도록 시간을 보낸 후 Mac 관용구로 전환하는 것을 고려해 보십시오. 이 설정을 사용하면 텍스트와 아트워크가 더 세부적으로 렌더링되고 일부 인터페이스 요소와 뷰는 훨씬 더 Mac과 같은 모양을 취합니다.
>




Apps that display a lot of text, detailed artwork, or use animations are most likely to benefit from this setting. Nevertheless, adopting the Mac idiom typically requires spending additional time to update your Mac app’s layout.
> 많은 텍스트, 세부 예술작품 또는 애니메이션을 사용하는 앱이 이 설정의 혜택을 받을 가능성이 가장 높습니다. 그럼에도 불구하고 Mac 관용구를 채택하려면 일반적으로 Mac 앱의 레이아웃을 업데이트하는 데 추가 시간이 필요합니다.
>




# **Review differences between the iPad and the Mac idiom**
> iPad와 Mac 관용구의 차이점 검토
>




One of the main differences between the iPad idiom and the Mac idiom is the appearance of iOS views and text. Specifically, iOS views and text scale down to 77% in macOS when you use the iPad idiom. When you adopt the Mac idiom to further optimize your Mac app, iOS views render at 100% of their size, and text and graphics appear more detailed.
> 아이패드 관용구와 맥 관용구의 주요 차이점 중 하나는 iOS 보기와 텍스트의 외관이다. 특히 iPad 관용구를 사용하면 iOS 보기와 텍스트가 MacOS에서 77%까지 축소됩니다. Mac 앱을 더욱 최적화하기 위해 Mac 관용구를 채택하면 iOS 보기가 크기의 100%로 렌더링되고 텍스트와 그래픽이 더 자세히 표시됩니다.
>




Below are two versions of an image asset. One version illustrates how the asset appears when you use the iPad idiom, and the other version shows how the asset appears when you adopt the Mac idiom. Both are zoomed in to show how the image renders with more details when you adopt the Mac idiom.
> 다음은 이미지 자산의 두 가지 버전입니다. 한 버전은 iPad 관용구를 사용할 때 자산이 어떻게 표시되는지 보여주고, 다른 버전은 Mac 관용구를 사용할 때 자산이 어떻게 표시되는지 보여줍니다. 둘 다 확대되어 Mac 관용구를 채택할 때 이미지가 더 자세히 렌더링되는 방식을 보여줍니다.
>




• [iPad idiom](../technologies/mac-catalyst/mac-idiom#)
• [Mac idiom](../technologies/mac-catalyst/mac-idiom#)

-

![https://developer.apple.com/design/human-interface-guidelines/technologies/mac-catalyst/images/ipad-idiom_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/mac-catalyst/images/ipad-idiom_2x.png)


In addition to displaying unscaled text and images, selecting the Mac idiom further optimizes your app to provide the best possible experience on the Mac; for example:
> 스케일이 지정되지 않은 텍스트와 이미지를 표시하는 것 외에도 Mac 관용구를 선택하면 Mac에서 가능한 최상의 환경을 제공할 수 있도록 앱이 더욱 최적화됩니다. 예를 들어 다음과 같습니다:
>




- Some iOS interface elements and views like buttons or the color well take on a more Mac-like appearance.
- >  일부 iOS 인터페이스 요소와 버튼이나 색상과 같은 보기는 Mac과 같은 외관을 가지고 있습니다.

- An iOS switch becomes a checkbox in macOS.
- >  iOS 스위치는 macOS에서 확인란이 됩니다.

- Controls and interface elements in macOS take advantage of wider macOS windows and use more horizontal padding and often take up more space.
- >  macOS의 제어와 인터페이스 요소는 더 넓은 macOS 창을 이용하고 더 많은 수평 패딩을 사용하며 종종 더 많은 공간을 차지한다.

- Graphics-intensive apps may see improved performance and lower power consumption.
- >  그래픽을 많이 사용하는 앱은 성능이 향상되고 전력 소비가 감소할 수 있습니다.


