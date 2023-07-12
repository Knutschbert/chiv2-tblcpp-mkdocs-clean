---
title: UHudMarkerDisplayComponent
type: class
aliases: UHudMarkerDisplayComponent
share: false

---

# UHudMarkerDisplayComponent





Inherits from [UDisplayComponent](/docs/SDK/Source/Classes/classUDisplayComponent.md), [IPlayerInHudMarkerZoneInterface](/docs/SDK/Source/Classes/classIPlayerInHudMarkerZoneInterface.md), UActorComponent, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md), [IDisplayComponentInterface](/docs/SDK/Source/Classes/classIDisplayComponentInterface.md)

Inherited by [USubObjectiveZoneDisplayComponent](/docs/SDK/Source/Classes/classUSubObjectiveZoneDisplayComponent.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[Add]]**(AActor * Actor) |
| void | **[[AddPlayerToPlayerVisibilityList]]**([ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * Player) |
| void | **[[ForceUsePerTeamDisplayInfo]]**() |
| AActor * | **[[GetActorToDisplayInfoFor]]**() |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| EObjectiveState | **[[GetObjectiveState]]**() |
| FText | **[[GetObjectiveStateText]]**(EFaction Faction) |
| EFaction | **[[GetOwningTeam]]**() |
| float | **[[GetProgress]]**() const |
| [FActorDisplayInfo](/docs/SDK/Source/Classes/structFActorDisplayInfo.md) | **[[GetRelevantDisplayInfo]]**(EFaction Faction, bool bFlip) |
| FVector | **[[GetScreenLocation]]**(APlayerController * PlayerController, const FVector2D & WidgetSize, bool & bIsOnScreen, bool & bWasClamped) const |
| bool | **[[GetVisible]]**() const |
| TArray< [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * > | **[[GetVisibleToPlayersList]]**() |
| [UWidgetVisibilityComponent](/docs/SDK/Source/Classes/classUWidgetVisibilityComponent.md) * | **[[GetWidgetVisibilityComponent]]**() |
| virtual bool | **[[IsLocalPlayerInHudMarkerZone]]**() override |
| bool | **[[IsVisible]]**() const |
| bool | **[[IsVisibleFor]]**(APlayerController * PlayerController, bool bCheckVisiblityComponent, bool bVerboseLogging) const |
| void | **[[OnPlayerStateReplicated]]**(APlayerState * PS) |
| void | **[[OnPlayerTeamReplicated]]**([ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * Team) |
| void | **[[OnRep_ObjectiveState]]**() |
| void | **[[OnRep_ObjectiveStateText]]**() |
| void | **[[OnRep_OwningTeam]]**() |
| void | **[[OnRep_Progress]]**() |
| void | **[[OnRep_Visible]]**() |
| void | **[[OnRep_VisibleToTeam]]**() |
| void | **[[RemovePlayerFromPlayerVisibilityList]]**([ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * Player) |
| void | **[[SetActiveIcon]]**(UMaterialInstance * NewIcon) |
| void | **[[SetActorToDisplayInfoFor]]**(AActor * Actor) |
| void | **[[SetObjectiveState]]**(EObjectiveState Value) |
| void | **[[SetObjectiveStateText]]**(EFaction Faction, FText Value) |
| void | **[[SetOwningTeam]]**(EFaction Value) |
| void | **[[SetPerTeamDisplayInfo]]**(const TArray< [FActorDisplayInfo](/docs/SDK/Source/Classes/structFActorDisplayInfo.md) > & InPerTeamDisplayInfo) |
| void | **[[SetProgress]]**(float Value) |
| void | **[[SetVisible]]**(bool Value) |
| void | **[[SetVisibleToTeam]]**(EFaction NewTeam) |
| void | **[[SetWidgetVisibilityComponent]]**([UWidgetVisibilityComponent](/docs/SDK/Source/Classes/classUWidgetVisibilityComponent.md) * InWidgetVisibilityComponent) |
| bool | **[[ShouldClampToScreen]]**() const |
| bool | **[[ShouldForceUsePerTeamDisplayInfo]]**() const |
| | **[[UHudMarkerDisplayComponent]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| UMaterialInstance * | **[[ActiveObjectiveIcon]]**  |
| [FReplicated_AActorPtr](/docs/SDK/Source/Classes/structFReplicated__AActorPtr.md) | **[[ActorToDisplayInfoFor]]**  |
| [FReplicated_FText](/docs/SDK/Source/Classes/structFReplicated__FText.md) | **[[AgathaText]]**  |
| UMaterialInstance * | **[[ContestedObjectiveIcon]]**  |
| AActor * | **[[DefaultActorToDisplayInfoFor]]**  |
| FText | **[[DefaultAgathaText]]**  |
| FText | **[[DefaultMasonText]]**  |
| EObjectiveState | **[[DefaultObjectiveState]]**  |
| EFaction | **[[DefaultOwningTeam]]**  |
| float | **[[DefaultProgress]]**  |
| FText | **[[DefaultTenosiaText]]**  |
| UCurveFloat * | **[[DistAlphaCurve]]**  |
| UCurveFloat * | **[[DistScaleCurve]]**  |
| TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[InventoryItemClass]]**  |
| EFaction | **[[ItemVisibilityRelevantFaction]]**  |
| EMarkerType | **[[MarkerType]]**  |
| [FReplicated_FText](/docs/SDK/Source/Classes/structFReplicated__FText.md) | **[[MasonText]]**  |
| float | **[[MaxFocusDist]]**  |
| float | **[[MaxVisibleDistance]]**  |
| float | **[[MinFocusDist]]**  |
| float | **[[MinVisibleDistance]]**  |
| float | **[[MinimumFriendPartyMemberScale]]**  |
| TSubclassOf< [ASiegeEngine](/docs/SDK/Source/Classes/classASiegeEngine.md) > | **[[MountClass]]**  |
| EMountVisibilityCondition | **[[MountVisibilityCondition]]**  |
| [FReplicated_EObjectiveState](/docs/SDK/Source/Classes/structFReplicated__EObjectiveState.md) | **[[ObjectiveState]]**  |
| FHUDMarkerDisplayUpdateSignature | **[[OnForceUsePerTeamDisplayInfo]]**  |
| FOnHudMarkerComponentVisibilityChanged | **[[OnHudMarkerComponentVisibilityChanged]]**  |
| FObjectiveStateChanged | **[[OnObjectiveStateChanged]]**  |
| FObjectiveStateTextChanged | **[[OnObjectiveStateTextChanged]]**  |
| FOwningTeamChanged | **[[OnOwningTeamChanged]]**  |
| FPerTeamDisplayInfoChangedSignature | **[[OnPerTeamDisplayInfoChanged]]**  |
| FProgressChanged | **[[OnProgressChanged]]**  |
| FOnReceivedWidgetVisibilityComponent | **[[OnReceivedWidgetVisibilityComponent]]**  |
| [FReplicated_EFaction](/docs/SDK/Source/Classes/structFReplicated__EFaction.md) | **[[OwningTeam]]**  |
| TArray< [FActorDisplayInfo](/docs/SDK/Source/Classes/structFActorDisplayInfo.md) > | **[[PerTeamDisplayInfo]]**  |
| UCurveFloat * | **[[PercentFromCenterAlphaCurve]]**  |
| UCurveFloat * | **[[PercentFromCenterDistanceModifier]]**  |
| UCurveFloat * | **[[PercentFromCenterScaleCurve]]**  |
| EFaction | **[[PlayerVisiblityByFaction]]**  |
| [FReplicated_Float](/docs/SDK/Source/Classes/structFReplicated__Float.md) | **[[Progress]]**  |
| FVector | **[[RelativeLocation]]**  |
| bool | **[[ShowProgress]]**  |
| bool | **[[StartVisible]]**  |
| [FReplicated_FText](/docs/SDK/Source/Classes/structFReplicated__FText.md) | **[[TenosiaText]]**  |
| EInventoryVisibilityCondition | **[[VisibilityCondition]]**  |
| [FReplicated_Bool](/docs/SDK/Source/Classes/structFReplicated__Bool.md) | **[[Visible]]**  |
| bool | **[[VisibleEvenOnOwnPawn]]**  |
| float | **[[VisibleRadius]]**  |
| [FReplicatedArray_ATBLPlayerStatePtr](/docs/SDK/Source/Classes/structFReplicatedArray__ATBLPlayerStatePtr.md) | **[[VisibleToPlayers]]**  |
| EFaction | **[[VisibleToTeam]]**  |
| [FReplicated_EFaction](/docs/SDK/Source/Classes/structFReplicated__EFaction.md) | **[[VisibleToTeamRep]]**  |
| TWeakObjectPtr< [UWidgetVisibilityComponent](/docs/SDK/Source/Classes/classUWidgetVisibilityComponent.md) > | **[[WidgetVisibilityComponent]]**  |
| bool | **[[bForceUsePerTeamDisplayInfo]]**  |
| bool | **[[bIsFocusMarker]]**  |
| bool | **[[bLocalPlayerInsideZone]]**  |
| bool | **[[bOnlyFocusInLos]]**  |
| bool | **[[bOnlyRenderInLos]]**  |
| bool | **[[bUseActorLocation]]**  |
| bool | **[[bUseItemVisibility]]**  |
| bool | **[[bUseMountVisibility]]**  |
| bool | **[[bUseRelativeAsWorldOffset]]**  |
| bool return | **[[false]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| bool | **[[bClampToScreen]]**  |
| bool | **[[bWantsToBeReplicated]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200