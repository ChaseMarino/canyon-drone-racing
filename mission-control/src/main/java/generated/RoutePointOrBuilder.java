// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: Route.proto

package generated;

public interface RoutePointOrBuilder extends
    // @@protoc_insertion_point(interface_extends:tutorial.RoutePoint)
    com.google.protobuf.MessageOrBuilder {

  /**
   * <code>.tutorial.Location location = 1;</code>
   * @return Whether the location field is set.
   */
  boolean hasLocation();
  /**
   * <code>.tutorial.Location location = 1;</code>
   * @return The location.
   */
  generated.Location getLocation();
  /**
   * <code>.tutorial.Location location = 1;</code>
   */
  generated.LocationOrBuilder getLocationOrBuilder();

  /**
   * <code>float speed = 2;</code>
   * @return The speed.
   */
  float getSpeed();
}