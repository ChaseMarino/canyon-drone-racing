// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: Command.proto

public interface CommandOrBuilder extends
    // @@protoc_insertion_point(interface_extends:Command)
    com.google.protobuf.MessageOrBuilder {

  /**
   * <code>bytes uuid = 1;</code>
   * @return The uuid.
   */
  com.google.protobuf.ByteString getUuid();

  /**
   * <code>.Command.TakeoffCommand takeoff = 2;</code>
   * @return Whether the takeoff field is set.
   */
  boolean hasTakeoff();
  /**
   * <code>.Command.TakeoffCommand takeoff = 2;</code>
   * @return The takeoff.
   */
  Command.TakeoffCommand getTakeoff();
  /**
   * <code>.Command.TakeoffCommand takeoff = 2;</code>
   */
  Command.TakeoffCommandOrBuilder getTakeoffOrBuilder();

  /**
   * <code>.Command.LandCommand land = 3;</code>
   * @return Whether the land field is set.
   */
  boolean hasLand();
  /**
   * <code>.Command.LandCommand land = 3;</code>
   * @return The land.
   */
  Command.LandCommand getLand();
  /**
   * <code>.Command.LandCommand land = 3;</code>
   */
  Command.LandCommandOrBuilder getLandOrBuilder();

  /**
   * <code>.Command.MoveToCommand moveTo = 4;</code>
   * @return Whether the moveTo field is set.
   */
  boolean hasMoveTo();
  /**
   * <code>.Command.MoveToCommand moveTo = 4;</code>
   * @return The moveTo.
   */
  Command.MoveToCommand getMoveTo();
  /**
   * <code>.Command.MoveToCommand moveTo = 4;</code>
   */
  Command.MoveToCommandOrBuilder getMoveToOrBuilder();

  /**
   * <code>.Command.MoveGimbalCommand moveGimbal = 5;</code>
   * @return Whether the moveGimbal field is set.
   */
  boolean hasMoveGimbal();
  /**
   * <code>.Command.MoveGimbalCommand moveGimbal = 5;</code>
   * @return The moveGimbal.
   */
  Command.MoveGimbalCommand getMoveGimbal();
  /**
   * <code>.Command.MoveGimbalCommand moveGimbal = 5;</code>
   */
  Command.MoveGimbalCommandOrBuilder getMoveGimbalOrBuilder();

  /**
   * <code>.Command.ChangeZoomLevelCommand changeZoomLevel = 6;</code>
   * @return Whether the changeZoomLevel field is set.
   */
  boolean hasChangeZoomLevel();
  /**
   * <code>.Command.ChangeZoomLevelCommand changeZoomLevel = 6;</code>
   * @return The changeZoomLevel.
   */
  Command.ChangeZoomLevelCommand getChangeZoomLevel();
  /**
   * <code>.Command.ChangeZoomLevelCommand changeZoomLevel = 6;</code>
   */
  Command.ChangeZoomLevelCommandOrBuilder getChangeZoomLevelOrBuilder();

  /**
   * <code>.Command.GetPositionCommand getPosition = 7;</code>
   * @return Whether the getPosition field is set.
   */
  boolean hasGetPosition();
  /**
   * <code>.Command.GetPositionCommand getPosition = 7;</code>
   * @return The getPosition.
   */
  Command.GetPositionCommand getGetPosition();
  /**
   * <code>.Command.GetPositionCommand getPosition = 7;</code>
   */
  Command.GetPositionCommandOrBuilder getGetPositionOrBuilder();

  /**
   * <code>.Command.GetOrientationCommand getOrientation = 8;</code>
   * @return Whether the getOrientation field is set.
   */
  boolean hasGetOrientation();
  /**
   * <code>.Command.GetOrientationCommand getOrientation = 8;</code>
   * @return The getOrientation.
   */
  Command.GetOrientationCommand getGetOrientation();
  /**
   * <code>.Command.GetOrientationCommand getOrientation = 8;</code>
   */
  Command.GetOrientationCommandOrBuilder getGetOrientationOrBuilder();

  /**
   * <code>.Command.GetConnectionStateCommand getConnectionState = 9;</code>
   * @return Whether the getConnectionState field is set.
   */
  boolean hasGetConnectionState();
  /**
   * <code>.Command.GetConnectionStateCommand getConnectionState = 9;</code>
   * @return The getConnectionState.
   */
  Command.GetConnectionStateCommand getGetConnectionState();
  /**
   * <code>.Command.GetConnectionStateCommand getConnectionState = 9;</code>
   */
  Command.GetConnectionStateCommandOrBuilder getGetConnectionStateOrBuilder();

  public Command.CommandCase getCommandCase();
}