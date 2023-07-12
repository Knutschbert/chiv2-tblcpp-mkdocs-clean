---
title: UTBLCheatManager
type: class
aliases: UTBLCheatManager
share: false

---

# UTBLCheatManager





Inherits from UCheatManager

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[AIObjectiveHere]]**() |
| void | **[[AKStartProfilerCapture]]**(const FString & Filename) |
| void | **[[AKStopProfilerCapture]]**() |
| void | **[[AddAchievementProgress]]**() |
| void | **[[ApplyCondition]]**(FName Condition) |
| void | **[[ApplyDamage]]**(float Damage, FName DamageType) |
| void | **[[ApplyStatBonus]]**(EStat Stat, float Value) |
| void | **[[AutoAttack]]**(FName AttackName) |
| void | **[[AutoAttackClear]]**() |
| void | **[[AutoAttackEx]]**(FName AttackName, float ChargeTime, float LoopTime) |
| void | **[[AutoAttackHold]]**(FName AttackName) |
| void | **[[AutoClimbLadder]]**(float Direction) |
| void | **[[AutoMoveToCharacter]]**(bool bEnable) |
| void | **[[AutoRunAway]]**(bool bEnable) |
| void | **[[BlueprintDebugMenu]]**() |
| void | **[[BotForceMoveToPlayer]]**(int32 Team, int32 bClearOtherForcedMoves) |
| void | **[[BotGodsBecomeMortal]]**() |
| void | **[[BotNearestForceMoveToPlayer]]**(int32 Team) |
| void | **[[BotsBecomeGods]]**() |
| bool | **[[BpCheat]]**(const FString & Cmd) |
| void | **[[CheckLightingBuilt]]**() |
| void | **[[ClearAllForceMoveToPlayer]]**(int32 Team) |
| void | **[[ClearCharacterRuntimeAssetCache]]**() |
| void | **[[ClearReplicationCounts]]**() |
| void | **[[ClientBot]]**() |
| void | **[[ClientForceGC]]**() |
| void | **[[CloseBlueprintDebugMenu]]**() |
| void | **[[DebugHideLoadingScreen]]**() |
| void | **[[DebugShowLoadingScreen]]**(const FString & MapName) |
| void | **[[DestroyAllForcedMoveForTeam]]**(int32 Team) |
| void | **[[DestroyClientBot]]**() |
| void | **[[DisableHUDPostProcess]]**() |
| void | **[[DisableStaminaDrain]]**() |
| void | **[[DrawUnits]]**(float Distance) |
| void | **[[DumpCharacterReplicationCounts]]**() |
| void | **[[DumpCharacters]]**() |
| void | **[[DumpPlayers]]**() |
| void | **[[DumpReplicationCounts]]**() |
| void | **[[EnableHUDPostProcess]]**() |
| void | **[[ExecFile]]**(const FString & Filename) |
| void | **[[ExecFileDelay]]**(float Time, float Variation) |
| void | **[[Exi]]**(const FString & Cmd) |
| void | **[[FakeGameIntent]]**(const FString & ActivityId) |
| void | **[[ForceGC]]**() |
| void | **[[GiveArmoredHorse]]**() |
| void | **[[GiveHorse]]**() |
| void | **[[GoToStatePlaying]]**() |
| void | **[[GotoState]]**(FName CombatState, FName HitDirection, int32 Variant) |
| void | **[[HideBothMeshes]]**() |
| void | **[[HideDebugActor]]**() |
| void | **[[HorseAutorun]]**(bool bEnable) |
| void | **[[HorseGotoState]]**(FName CombatState, FName HitDirection, int32 Variant) |
| void | **[[Invulnerable]]**() |
| bool | **[[IsAutoAttacking]]**() const |
| bool | **[[IsFOVUncapped]]**() const |
| void | **[[KillHorse]]**() |
| void | **[[LoadAllCustomizationAssets]]**() |
| void | **[[LoadCatapult]]**() |
| void | **[[LoseHelmet]]**() |
| void | **[[ManualInterrupt]]**() |
| void | **[[MergeMaterials]]**() |
| void | **[[MergeMeshes]]**() |
| void | **[[NextLatentCommand]]**() |
| void | **[[OnKilled]]**() |
| void | **[[OnPossess]]**() |
| void | **[[PauseAI]]**() |
| void | **[[PauseCharacter]]**() |
| void | **[[PingServer]]**(const FString & ServerAddress) |
| void | **[[PlayFromHere]]**() |
| void | **[[PlayerRVODisable]]**() |
| void | **[[PlayerRVOEnable]]**(float AvoidanceRadius) |
| void | **[[PrintStats]]**() |
| void | **[[ProfileGpuTopMaterials]]**() |
| void | **[[PromptForRemoteDebugging]]**() |
| void | **[[PushCmd]]**(const FString & Cmd) |
| void | **[[PushCmdToTrace]]**(const FString & Cmd) |
| void | **[[PushLogs]]**(const FString & SourcePath, const FString & DestPath) |
| void | **[[RandomizeLoadout]]**(bool bEnable) |
| void | **[[ReceivedCheatFromClient]]**(FName CheatCommand, FName Param) |
| void | **[[ReceivedCheatFromClientObj]]**(FName CheatCommand, UObject * Param) |
| void | **[[RechargeSpecialItem]]**() |
| void | **[[RemoveStamina]]**() |
| void | **[[RespawnImmediately]]**() |
| void | **[[RespawnLoadout]]**() |
| void | **[[Revive]]**() |
| void | **[[SaveAll]]**(const FString & ClassName) |
| void | **[[SendToAll]]**(const FString & Command) |
| void | **[[SendToTrace]]**(const FString & Command) |
| void | **[[SetAmmo]]**(int32 Ammo) |
| void | **[[SetCulture]]**(const FString & Culture) |
| void | **[[SetHealth]]**(float Value) |
| void | **[[SetStatBase]]**(EStat Stat, float Value) |
| void | **[[SetWatchedCharacter]]**() |
| void | **[[ShowBothMeshes]]**() |
| void | **[[ShowFirstPersonMesh]]**() |
| void | **[[ShowServerFollowMesh]]**() |
| void | **[[ShowThirdPersonMesh]]**() |
| void | **[[SimulateLostServerConnection]]**() |
| void | **[[SkipPushableToEndPoint]]**(UObject * PushableActor) |
| void | **[[SpamRPC]]**(int32 NumCalls, int32 NumBytesPerCall) |
| void | **[[SpawnAsPeasant]]**() |
| void | **[[StartDumpingReplication]]**() |
| void | **[[StartHeldParry]]**() |
| void | **[[StopAllSounds]]**() |
| void | **[[StopDumpingReplication]]**() |
| void | **[[StopExecFile]]**() |
| void | **[[StopHeldParry]]**() |
| void | **[[TestDrawTime]]**() |
| void | **[[TestRPCDesync]]**() |
| void | **[[Tick]]**(float DeltaTime) |
| void | **[[ToggleCameraAnimsAndShakes]]**() |
| void | **[[ToggleShowBothMeshes]]**() |
| | **[[UTBLCheatManager]]**() |
| void | **[[UncapFOV]]**() |
| void | **[[UnlimitedAmmo]]**() |
| void | **[[UnpauseAI]]**() |
| void | **[[UnpauseCharacter]]**() |
| void | **[[UpdateVirtualGood]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[AutoAttackClearInternal]]**() |
| void | **[[AutoAttackEndCharge]]**() |
| void | **[[AutoAttackLoop]]**() |
| void | **[[AutoAttackStart]]**(FName AttackName, float ChargeTime, float LoopTime) |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[GetAnotherCharacter]]**() |
| void | **[[GotoStateOnComponent]]**([UCombatStateComponent](/docs/SDK/Source/Classes/classUCombatStateComponent.md) * Component, FName CombatState, FName HitDirection, int32 Variant) |
| void | **[[HeldParryLoop]]**() |
| void | **[[IgnoreAI]]**() |
| void | **[[InputAction]]**(FName AttackName, TEnumAsByte< EInputEvent > Event) |
| void | **[[ResetHeldParry]]**() |
| void | **[[SendCheatToServer]]**(FName CheatComand, FName Param) |
| void | **[[SendCheatToServerObj]]**(FName CheatComand, UObject * Obj) |
| void | **[[SetPauseAI]]**(bool bPaused) |
| void | **[[SetPauseCharacter]]**(bool bPaused) |
| void | **[[SetPawnRVO]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character, bool bEnabled) |
| void | **[[UpdateAutoAttackHold]]**() |
| void | **[[UpdateExecFileCommands]]**(float DeltaTime) |
| void | **[[UpdateMoveToCharacter]]**(float DeltaTime) |
| void | **[[UpdateRunAway]]**(float DeltaTime) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TSoftClassPtr< [UTBLBPCheatManager](/docs/SDK/Source/Classes/classUTBLBPCheatManager.md) > | **[[BPCheatManagerClass]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| float | **[[AutoAttackChargeTime]]**  |
| FName | **[[AutoAttackHoldName]]**  |
| float | **[[AutoAttackLoopTime]]**  |
| FName | **[[AutoAttackName]]**  |
| float | **[[AutoClimbDirection]]**  |
| [UTBLBPCheatManager](/docs/SDK/Source/Classes/classUTBLBPCheatManager.md) * | **[[BPCheatManager]]**  |
| [ATBLAIController](/docs/SDK/Source/Classes/classATBLAIController.md) * | **[[ClientAIController]]**  |
| TArray< FString > | **[[ExecFileCommands]]**  |
| float | **[[ExecFileDelayTime]]**  |
| TArray< FName > | **[[ParryAbilities]]**  |
| float | **[[PlayerRVOConsiderationRadius]]**  |
| TArray< FName > | **[[RandomAttacks]]**  |
| bool | **[[bDisableStaminaDrain]]**  |
| bool | **[[bGodMode]]**  |
| bool | **[[bInvulnerable]]**  |
| bool | **[[bIsAutoAttack]]**  |
| bool | **[[bIsFOVUncapped]]**  |
| bool | **[[bIsHeldParry]]**  |
| bool | **[[bMoveToCharacter]]**  |
| bool | **[[bPlayerRVOEnabled]]**  |
| bool | **[[bRandomAttack]]**  |
| bool | **[[bRandomizeLoadout]]**  |
| bool | **[[bRunAway]]**  |
| bool | **[[bUnlimitedAmmo]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200