# **[technologies] wallet**

# Wallet helps people securely store their credit and debit cards, driver’s license or state ID, transit cards, event tickets, keys, and more on iPhone and Apple Watch.
> 지갑은 사람들이 신용카드와 직불카드, 운전면허증이나 신분증, 교통카드, 이벤트 티켓, 열쇠 등을 아이폰과 애플워치에 안전하게 저장할 수 있도록 도와준다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-Wallet-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-Wallet-intro_2x.png)

People use their cards and passes in Wallet to make Apple Pay — and Apple Pay Later — purchases, track their orders, confirm their identity, and streamline activities like boarding a plane, attending a concert, or receiving a discount.
> 사람들은 애플 페이(Apple Pay)와 애플 페이 라이터(Apple Pay Later)를 구매하고, 주문을 추적하고, 신원을 확인하며, 비행기 탑승, 콘서트 참석 또는 할인과 같은 활동을 간소화하기 위해 자신의 카드와 패스를 사용합니다.
>




When you integrate Apple Wallet into your app, you can create custom passes and present them the moment people need them, securely verify an individual’s identity so they can access personal content, and offer detailed receipts and tracking information where it’s most convenient. For developer guidance, see [Wallet](https://developer.apple.com/documentation/passkit/wallet).
> Apple Wallet을 앱에 통합하면 사용자 지정 패스를 생성하여 필요한 순간에 제시하고, 개인 컨텐츠에 액세스할 수 있도록 개인의 신원을 안전하게 확인하고, 가장 편리한 곳에서 상세한 영수증 및 추적 정보를 제공할 수 있습니다. 개발자 지침은 지갑을 참조하십시오.
>




# **Passes**

**Offer to add new passes to Wallet.** When people do something that results in a new pass — like checking into a flight, purchasing an event ticket, or registering for a store reward program — you can present system-provided UI that helps them add the pass to Wallet with one tap (for developer guidance, see [addPasses(_:withCompletionHandler:)](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617093-addpasses)). If people want to review a pass before adding it, you can display a custom view that displays the pass and provides an Add to Apple Wallet button; for developer guidance, see [PKAddPassesViewController](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontroller).
> 사람들이 비행기 탑승 수속, 이벤트 티켓 구입, 상점 보상 프로그램 등록 등 새로운 패스를 할 때 한 번의 탭으로 월렛에 패스를 추가할 수 있는 시스템 제공 UI를 제시할 수 있습니다(개발자 지침은 패스 추가(_:CompletionHandler:)). 사용자가 패스를 추가하기 전에 확인하려는 경우 패스를 표시하고 Apple Wallet에 추가 단추를 제공하는 사용자 정의 뷰를 표시할 수 있습니다. 개발자 지침은 PKAddPassesViewController를 참조하십시오.
>




**Help people add a pass that they created outside of your app.** If people create a pass using your website or another device, suggest adding it to Wallet the next time they open your app. If people decline your suggestion, don’t ask them again.
> 다른 사람들이 당신의 앱 밖에서 만든 패스를 추가할 수 있도록 도와줍니다. 만약 사람들이 당신의 웹사이트나 다른 기기를 사용하여 패스를 만든다면, 그들이 다음에 당신의 앱을 열 때 지갑에 그것을 추가할 것을 제안합니다. 만약 사람들이 당신의 제안을 거절한다면, 그들에게 다시 묻지 마세요.
>




**Add related passes as a group.** If your app generates multiple passes, like boarding passes for a multi-connection flight, add all passes at the same time so people don’t have to add each one individually. If people can receive a group of passes from your website — such as a set of tickets for an event — bundle them together so that people can download all of them at one time. For developer guidance, see [Distributing and updating a pass](https://developer.apple.com/documentation/walletpasses/distributing_and_updating_a_pass).
> 단체로 관련 패스를 추가합니다. 다중 연결 항공편의 탑승권과 같이 앱에서 여러 개의 패스를 생성하는 경우, 사람들이 개별적으로 추가할 필요가 없도록 모든 패스를 동시에 추가하십시오. 이벤트 티켓 세트와 같은 사용자가 웹 사이트에서 패스 그룹을 받을 수 있는 경우 한 번에 모든 패스를 다운로드할 수 있도록 패스 그룹을 함께 묶습니다. 개발자 지침은 패스 배포 및 업데이트를 참조하십시오.
>




**Display an Add to Apple Wallet button to let people add an existing pass that isn’t already in Wallet.** If people previously declined your suggestion to add a pass to Wallet — or if they removed the pass — a button makes it easy to add it if they change their minds. You can display an Add to Apple Wallet button wherever the corresponding pass information appears in your app. For developer guidance, see [PKAddPassButton](https://developer.apple.com/documentation/passkit/pkaddpassbutton). You can also display an Add to Apple Wallet badge in an email or on a webpage; for guidance, see [Add to Apple Wallet guidelines](https://developer.apple.com/wallet/add-to-apple-wallet-guidelines/).
> 아직 지갑에 없는 기존 패스를 추가할 수 있도록 하려면 Apple Wallet에 추가 단추를 표시합니다. 이전에 다른 사람이 지갑에 패스를 추가하라는 사용자의 제안을 거부했거나 패스를 제거한 경우 단추를 누르면 마음이 바뀌어도 쉽게 추가할 수 있습니다. Apple Wallet에 추가 버튼은 해당 패스 정보가 앱에 표시되는 곳마다 표시할 수 있습니다. 개발자 지침은 PKAddPassButton을 참조하십시오. 전자 메일이나 웹 페이지에 Apple Wallet에 추가 배지를 표시할 수도 있습니다. 자세한 내용은 Apple Wallet에 추가 지침을 참조하십시오.
>




**Let people jump from your app to their pass in Wallet.** Wherever your app displays information about a pass that exists in Wallet, you can offer a link that opens it directly. Label the link something like “View in Wallet.”
> 사람들이 당신의 앱에서 지갑의 그들의 패스로 점프할 수 있게 해주세요. 당신의 앱이 지갑에 존재하는 패스에 대한 정보를 표시하는 곳이라면, 당신은 그것을 직접 여는 링크를 제공할 수 있습니다. 링크에 "지갑에서 보기"와 같은 레이블을 지정합니다
>




