---
title: UTBLOnlineLibrary
type: class
aliases: UTBLOnlineLibrary
share: false

---

# UTBLOnlineLibrary





Inherits from UBlueprintFunctionLibrary

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[AcceptPartyInviteFromPlayer]]**([UTBLLocalPlayer](/docs/SDK/Source/Classes/classUTBLLocalPlayer.md) * InPlayer, const [FBlueprintOnlineUser](/docs/SDK/Source/Classes/structFBlueprintOnlineUser.md) & User) |
| void | **[[AcceptPartyInviteFromPlayerName]]**([UTBLLocalPlayer](/docs/SDK/Source/Classes/classUTBLLocalPlayer.md) * InPlayer, const FString & InviteeName) |
| void | **[[ActivateGameOverlayToWebPage]]**(const FString & URL) |
| void | **[[AddBlockFromBlueprintOnlineUser]]**([UTBLLocalPlayer](/docs/SDK/Source/Classes/classUTBLLocalPlayer.md) * InPlayer, const [FBlueprintOnlineUser](/docs/SDK/Source/Classes/structFBlueprintOnlineUser.md) & User) |
| void | **[[AddFriendFromBlueprintOnlineUser]]**([ATBLPlayerController](/docs/SDK/Source/Classes/classATBLPlayerController.md) * InController, const [FBlueprintOnlineUser](/docs/SDK/Source/Classes/structFBlueprintOnlineUser.md) & User) |
| bool | **[[AreWePartyHost]]**() |
| void | **[[BroadcastGameModeMessages]]**(TArray< [FGameModeMessageTable](/docs/SDK/Source/Classes/structFGameModeMessageTable.md) > GameModeMessages, UObject * WorldContextObject) |
| void | **[[BroadcastLocalizedChat]]**(FText Msg, TEnumAsByte< EChatType::Type > Type, EFaction ReceivingFaction, UObject * WorldContextObject) |
| void | **[[BroadcastLocalizedObjectiveMessage]]**(const [FObjectiveMessage](/docs/SDK/Source/Classes/structFObjectiveMessage.md) & ObjectiveMessage, EFaction ReceivingFaction, UObject * WorldContextObject) |
| bool | **[[CanJoinGame]]**(const [FBlueprintOnlineUser](/docs/SDK/Source/Classes/structFBlueprintOnlineUser.md) & User) |
| bool | **[[CanSendPartyInvites]]**() |
| bool | **[[CheckAppOwnership]]**() |
| UTexture * | **[[GetAvatarImageFromOnlineUser]]**(const [FBlueprintOnlineUser](/docs/SDK/Source/Classes/structFBlueprintOnlineUser.md) & User, ESteamAvatarSize Size) |
| UTexture * | **[[GetAvatarImageFromPlayerState]]**(APlayerState * PlayerState, ESteamAvatarSize Size) |
| FString | **[[GetDebugStringForSessionSettingsKey]]**(FName Key) |
| bool | **[[GetFriendById]]**(const FString & FriendId, [FBlueprintOnlineUser](/docs/SDK/Source/Classes/structFBlueprintOnlineUser.md) & OutBlueprintUser) |
| void | **[[GetListOfCurrentSessions]]**(TArray< FName > & CurrentSessions) |
| FString | **[[GetLocalPlayerId]]**() |
| FString | **[[GetMapName]]**(const FBlueprintSessionResult & Result) |
| int32 | **[[GetNumBots]]**(const FBlueprintSessionResult & Result) |
| int32 | **[[GetPartyMemberCount]]**() |
| void | **[[GetPartyMembers]]**(TArray< [FBlueprintOnlineUser](/docs/SDK/Source/Classes/structFBlueprintOnlineUser.md) > & OutPartyMembers) |
| void | **[[GetSessionSettingsAsStrings]]**(FName SessionName, TArray< FString > & Keys, TArray< FString > & Values) |
| void | **[[GetSessionSettingsKeys]]**(const FBlueprintSessionResult & Result, TArray< FName > & OutSettingKeys) |
| FString | **[[GetSessionSettingsValue]]**(const FBlueprintSessionResult & Result, FName Key) |
| bool | **[[GetStatFloat]]**([ATBLPlayerController](/docs/SDK/Source/Classes/classATBLPlayerController.md) * InController, EOnlineStat Stat, float & returnVal) |
| bool | **[[GetStatInt]]**([ATBLPlayerController](/docs/SDK/Source/Classes/classATBLPlayerController.md) * InController, EOnlineStat Stat, int32 & returnVal) |
| bool | **[[GetStatOriginalFloat]]**([ATBLPlayerController](/docs/SDK/Source/Classes/classATBLPlayerController.md) * InController, EOnlineStat Stat, float & returnVal) |
| bool | **[[GetStatOriginalInt]]**([ATBLPlayerController](/docs/SDK/Source/Classes/classATBLPlayerController.md) * InController, EOnlineStat Stat, int32 & returnVal) |
| bool | **[[GetStatRangeFromPlayerState]]**([ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * PlayerState, EOnlineStat OnlineStat, int32 & Level, int32 & PreviousLevelExperience, int32 & NextLevelExperience) |
| bool | **[[GetStatRangeInt]]**([ATBLPlayerController](/docs/SDK/Source/Classes/classATBLPlayerController.md) * InController, EOnlineStat OnlineStat, int32 & Level, int32 & PreviousLevelExperience, int32 & NextLevelExperience) |
| bool | **[[GetStatRangeIntFromExperience]]**(int32 InExperience, EOnlineStat OnlineStat, int32 & Level, int32 & PreviousLevelExperience, int32 & NextLevelExperience) |
| bool | **[[GetStatRangeIntFromLevel]]**(int32 InLevel, EOnlineStat OnlineStat, int32 & Start, int32 & End) |
| [UTBLGameInstance](/docs/SDK/Source/Classes/classUTBLGameInstance.md) * | **[[GetTBLGameInstance]]**(const UObject * WorldContextObject) |
| [ATBLGameSession](/docs/SDK/Source/Classes/classATBLGameSession.md) * | **[[GetTBLGameSession]]**(UObject * WorldContextObject) |
| void | **[[GetTalkingPlayers]]**(TArray< [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * > & OutPlayerStates, UObject * WorldContextObject) |
| void | **[[InviteUserToGame]]**(const [FBlueprintOnlineUser](/docs/SDK/Source/Classes/structFBlueprintOnlineUser.md) & User) |
| void | **[[InviteUserToParty]]**([UTBLLocalPlayer](/docs/SDK/Source/Classes/classUTBLLocalPlayer.md) * InPlayer, const [FBlueprintOnlineUser](/docs/SDK/Source/Classes/structFBlueprintOnlineUser.md) & User) |
| bool | **[[IsAdminBP]]**(APlayerController * Controller) |
| bool | **[[IsAppOwnershipTemporary]]**() |
| bool | **[[IsGameJoinable]]**() |
| bool | **[[IsInAParty]]**(const [FBlueprintOnlineUser](/docs/SDK/Source/Classes/structFBlueprintOnlineUser.md) & User) |
| bool | **[[IsInMatchmadeGame]]**() |
| bool | **[[IsInMyParty]]**([UTBLLocalPlayer](/docs/SDK/Source/Classes/classUTBLLocalPlayer.md) * InPlayer, const [FBlueprintOnlineUser](/docs/SDK/Source/Classes/structFBlueprintOnlineUser.md) & User) |
| bool | **[[IsLocalPlayerPartyLeader]]**() |
| bool | **[[IsOfficialServerBySessionResult]]**(const FBlueprintSessionResult & Result) |
| bool | **[[IsPartyLeader]]**(const [FBlueprintOnlineUser](/docs/SDK/Source/Classes/structFBlueprintOnlineUser.md) & User) |
| bool | **[[IsPasswordProtectedServerBySessionResult]]**(const FBlueprintSessionResult & Result) |
| bool | **[[IsPlayerTalking]]**(const FString & PlayerId, UObject * WorldContextObject) |
| bool | **[[IsTutorialServer]]**() |
| bool | **[[IsUserMyself]]**(const [FBlueprintOnlineUser](/docs/SDK/Source/Classes/structFBlueprintOnlineUser.md) & User) |
| void | **[[JoinGame]]**(const [FBlueprintOnlineUser](/docs/SDK/Source/Classes/structFBlueprintOnlineUser.md) & User, [ATBLPlayerController](/docs/SDK/Source/Classes/classATBLPlayerController.md) * LocalController) |
| void | **[[KickPlayer]]**([UTBLLocalPlayer](/docs/SDK/Source/Classes/classUTBLLocalPlayer.md) * InPlayer, const [FBlueprintOnlineUser](/docs/SDK/Source/Classes/structFBlueprintOnlineUser.md) & User) |
| void | **[[LeaveParty]]**([UTBLLocalPlayer](/docs/SDK/Source/Classes/classUTBLLocalPlayer.md) * InPlayer) |
| bool | **[[LocalUserHasLicenseToApp]]**(int32 AppId) |
| void | **[[OpenPartyInviteDialog]]**() |
| void | **[[RemoveBlockFromBlueprintOnlineUser]]**([UTBLLocalPlayer](/docs/SDK/Source/Classes/classUTBLLocalPlayer.md) * InPlayer, const [FBlueprintOnlineUser](/docs/SDK/Source/Classes/structFBlueprintOnlineUser.md) & User) |
| void | **[[RemoveFriendFromBlueprintOnlineUser]]**([ATBLPlayerController](/docs/SDK/Source/Classes/classATBLPlayerController.md) * InController, const [FBlueprintOnlineUser](/docs/SDK/Source/Classes/structFBlueprintOnlineUser.md) & User) |
| FString | **[[SessionInfoToDebugString]]**(const FBlueprintSessionResult & Result) |
| void | **[[SetMuteStateForRemotePlayer]]**(bool VoiceChatEnabled, [ATBLPlayerController](/docs/SDK/Source/Classes/classATBLPlayerController.md) * LocalController, [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * NewPlayer) |
| void | **[[TBLJoinGameSession]]**(const FBlueprintSessionResult & SessionResult, const FString & Password, UObject * WorldContextObject) |
| | **[[UTBLOnlineLibrary]]**() |
| void | **[[ViewProfileFromBlueprintOnlineUser]]**(const [FBlueprintOnlineUser](/docs/SDK/Source/Classes/structFBlueprintOnlineUser.md) & User) |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200