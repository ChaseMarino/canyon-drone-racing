// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: External.proto

public interface PointTaskOrBuilder extends
    // @@protoc_insertion_point(interface_extends:PointTask)
    com.google.protobuf.MessageOrBuilder {

  /**
   * <code>.GeoLocation2D location = 1;</code>
   * @return Whether the location field is set.
   */
  boolean hasLocation();
  /**
   * <code>.GeoLocation2D location = 1;</code>
   * @return The location.
   */
  GeoLocation2D getLocation();
  /**
   * <code>.GeoLocation2D location = 1;</code>
   */
  GeoLocation2DOrBuilder getLocationOrBuilder();

  /**
   * <code>.Orientation gimbalOrientation = 2;</code>
   * @return Whether the gimbalOrientation field is set.
   */
  boolean hasGimbalOrientation();
  /**
   * <code>.Orientation gimbalOrientation = 2;</code>
   * @return The gimbalOrientation.
   */
  Orientation getGimbalOrientation();
  /**
   * <code>.Orientation gimbalOrientation = 2;</code>
   */
  OrientationOrBuilder getGimbalOrientationOrBuilder();

  /**
   * <code>optional double headingDegrees = 3;</code>
   * @return Whether the headingDegrees field is set.
   */
  boolean hasHeadingDegrees();
  /**
   * <code>optional double headingDegrees = 3;</code>
   * @return The headingDegrees.
   */
  double getHeadingDegrees();

  /**
   * <code>double zoomLevel = 4;</code>
   * @return The zoomLevel.
   */
  double getZoomLevel();
}
