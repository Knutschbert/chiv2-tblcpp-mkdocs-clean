---
title: UTBLLocalPlayer
type: class
aliases: UTBLLocalPlayer
share: false

---

# UTBLLocalPlayer





Inherits from ULocalPlayer

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[AcceptFriendInvitationFromPlayerExec]]**(const FString & PlayerId) |
| void | **[[AcceptPartyInvitationFromPlayerExec]]**(const FString & PlayerName) |
| void | **[[AddBlock]]**(const FString & PlayerId, const FString & PlayerName) |
| void | **[[AddRecent]]**(const FString & PlayerId, const FString & PlayerName) |
| bool | **[[CanLinkEpicAccount]]**(int32 LocalUserNum) const |
| void | **[[CopyInfo]]**() |
| TArray< [FBlueprintOnlineUser](/docs/SDK/Source/Classes/structFBlueprintOnlineUser.md) > | **[[GetBPPartyMembers]]**() |
| ESlateInputMode | **[[GetCurrentSlateInputMode]]**() const |
| TArray< [FBlueprintOnlineUser](/docs/SDK/Source/Classes/structFBlueprintOnlineUser.md) > | **[[GetFriendList]]**() |
| bool | **[[GetIsPartyInMatchmakingQueue]]**() |
| FString | **[[GetNickname]]**() const |
| [FBlueprintOnlineUser](/docs/SDK/Source/Classes/structFBlueprintOnlineUser.md) | **[[GetOnlineUser]]**(const FString & ID) |
| void | **[[GetPartyLeaderExec]]**() |
| int32 | **[[GetPartyMemberCount]]**() |
| TArray< [FBlueprintOnlineUser](/docs/SDK/Source/Classes/structFBlueprintOnlineUser.md) > | **[[GetPendingPartyMembers]]**() |
| bool | **[[IsBlocked]]**(const FString & PlayerId, const FString & PlayerName) |
| bool | **[[IsEpicAccountLinked]]**(int32 LocalUserNum) const |
| bool | **[[IsInParty]]**() |
| bool | **[[IsPartyLeader]]**() |
| void | **[[JoinPartyExec]]**(const FString & PartyId) |
| void | **[[LeavePartyExec]]**() |
| void | **[[LinkEpicAccount]]**(int32 LocalUserNum, FOnEpicAccountLinkingComplete OnAccountLinkingComplete) |
| void | **[[ListBlocks]]**() const |
| void | **[[ListPartyInvitationsExec]]**() |
| void | **[[ListRecents]]**() const |
| void | **[[OnEnumerateCloudFilesComplete]]**(const FPlatformInterfaceDelegateResult & Result) |
| void | **[[OnReadUserFileComplete]]**(const FPlatformInterfaceDelegateResult & Result) |
| void | **[[PartyKickExec]]**(const FString & PlayerId) |
| void | **[[ReadFriendsLists]]**() |
| void | **[[RegenerateFriendInviteCode]]**() |
| void | **[[RejectFriendInvitationFromPlayer]]**(const FString & PlayerId) |
| void | **[[RejectPartyInvitationFromPlayer]]**(const FString & PlayerId) |
| void | **[[RemoveBlock]]**(const FString & PlayerId, const FString & PlayerName) |
| void | **[[RemoveFriend]]**(const FString & PlayerName) |
| FString | **[[RetrieveInviteCode]]**() |
| void | **[[SendFriendInvitationByInviteCode]]**(const FString & PlayerInviteCode, FOnFriendInviteSent OnFriendInviteSent) |
| void | **[[SendPartyInvitationToPlayerId]]**(const FString & PlayerId) |
| void | **[[SendPartyInvitationToPlayerIdExec]]**(const FString & PlayerId) |
| | **[[UTBLLocalPlayer]]**() |
| void | **[[UpdatePendingInvites]]**() |
| void | **[[WhatBuild]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [UCloudBlockRecentPlayers](/docs/SDK/Source/Classes/classUCloudBlockRecentPlayers.md) * | **[[CloudBlockRecentPlayers]]**  |
| FString | **[[MostRecentServerPassword]]**  |
| FOnAcceptPartyInvite | **[[OnAcceptPartyInvite]]**  |
| FOnFriendCodeUpdated | **[[OnFriendCodeUpdated]]**  |
| FOnFriendInvitesReceived | **[[OnFriendInvitesReceived]]**  |
| FOnFriendStatusUpdated | **[[OnFriendStatusUpdated]]**  |
| FOnFriendsListsUpdated | **[[OnFriendsListsUpdated]]**  |
| FOnFriendsUpdated | **[[OnFriendsUpdated]]**  |
| FOnPartyCreated | **[[OnPartyCreatedResult]]**  |
| FOnPartyDisband | **[[OnPartyDisband]]**  |
| FOnPartyInviteAccept | **[[OnPartyInviteAccept]]**  |
| FOnnLocalPlayerPartyInviteResponseReceived | **[[OnPartyInviteResponseReceived]]**  |
| FOnPartyInviteSendResult | **[[OnPartyInviteSendResult]]**  |
| FOnPartyInviteSent | **[[OnPartyInviteSent]]**  |
| FOnLocalPlayerPartyInvitesChanged | **[[OnPartyInvitesChanged]]**  |
| FOnPartyInvitesReceived | **[[OnPartyInvitesReceived]]**  |
| FOnPartyJoinedQueue_Dynamic | **[[OnPartyJoinedQueue]]**  |
| FOnPartyLeaderChange | **[[OnPartyLeaderChange]]**  |
| FOnPartyLeave | **[[OnPartyLeave]]**  |
| FOnPartyLeftQueue_Dynamic | **[[OnPartyLeftQueue]]**  |
| FOnPartyMemberJoin | **[[OnPartyMemberJoin]]**  |
| FOnPartyMemberKick | **[[OnPartyMemberKick]]**  |
| FOnPartyMemberLeave | **[[OnPartyMemberLeave]]**  |
| FOnPartyMemberRemove | **[[OnPartyMemberRemove]]**  |
| FOnPartyMembersUpdated | **[[OnPartyMembersUpdated]]**  |
| FOnTitleBroadcastReceived | **[[OnTitleBroadcastReceived]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [UTBLScreenManager](/docs/SDK/Source/Classes/classUTBLScreenManager.md) * | **[[ActiveScreenManager]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200