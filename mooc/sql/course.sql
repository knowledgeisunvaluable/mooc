/*
 Navicat Premium Data Transfer

 Source Server         : connection
 Source Server Type    : MySQL
 Source Server Version : 80027
 Source Host           : localhost:3306
 Source Schema         : course

 Target Server Type    : MySQL
 Target Server Version : 80027
 File Encoding         : 65001

 Date: 15/07/2022 23:27:41
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for course_course
-- ----------------------------
DROP TABLE IF EXISTS `course_course`;
CREATE TABLE `course_course`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `desc` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL,
  `detail` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL,
  `learn_times` int(0) NULL DEFAULT NULL,
  `students_number` int(0) NULL DEFAULT NULL,
  `fav_nums` int(0) NULL DEFAULT NULL,
  `image` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL,
  `click_nums` int(0) NULL DEFAULT NULL,
  `category` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL,
  `tag` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL,
  `youneed_know` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL,
  `teacher_tell` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL,
  `add_time` datetime(6) NULL DEFAULT NULL,
  `bill` int(0) NULL DEFAULT NULL,
  `teacher_id` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of course_course
-- ----------------------------
INSERT INTO `course_course` VALUES (1, '111', '', '', 0, 0, 0, '', NULL, '1', NULL, '', '', NULL, 3, 0);
INSERT INTO `course_course` VALUES (9, '222', '', '', 0, 0, 0, '', NULL, '', NULL, '', '', NULL, 3, 0);
INSERT INTO `course_course` VALUES (10, '333', '', '', 0, 0, 0, '', NULL, '', NULL, '', '', NULL, 3, 0);
INSERT INTO `course_course` VALUES (12, '', '', '', 0, 0, 0, '', NULL, '', NULL, '', '', '2022-07-14 13:56:19.278322', 3, 0);
INSERT INTO `course_course` VALUES (114515, '1145141', '', '', 0, 0, 0, '', NULL, '', NULL, '', '', '2022-07-15 12:23:56.903512', 3, 0);
INSERT INTO `course_course` VALUES (114516, '11415141', '', '', 1, 0, 0, '', NULL, '', NULL, '', '', '2022-07-15 12:24:03.637462', 3, 0);

-- ----------------------------
-- Table structure for course_courseresource
-- ----------------------------
DROP TABLE IF EXISTS `course_courseresource`;
CREATE TABLE `course_courseresource`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL,
  `download` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL,
  `add_time` datetime(6) NULL DEFAULT NULL,
  `course_id` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `course_id`(`course_id`) USING BTREE,
  CONSTRAINT `course_courseresource_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `course_course` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 114520 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of course_courseresource
-- ----------------------------
INSERT INTO `course_courseresource` VALUES (114514, '33', 'Diana.jpg', '2022-06-01 21:08:45.000000', 1);
INSERT INTO `course_courseresource` VALUES (114516, '333', '114514', '2022-07-14 13:11:18.334226', 1);

-- ----------------------------
-- Table structure for course_coursestudent
-- ----------------------------
DROP TABLE IF EXISTS `course_coursestudent`;
CREATE TABLE `course_coursestudent`  (
  `student_id` int(0) NOT NULL,
  `course_id` int(0) NOT NULL,
  `id` int(0) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of course_coursestudent
-- ----------------------------
INSERT INTO `course_coursestudent` VALUES (11, 1, 114514);
INSERT INTO `course_coursestudent` VALUES (22, 1, 114515);

-- ----------------------------
-- Table structure for course_coursetag
-- ----------------------------
DROP TABLE IF EXISTS `course_coursetag`;
CREATE TABLE `course_coursetag`  (
  `course_id` int(0) NOT NULL,
  `course_tag` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `id` int(0) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `course_id`(`course_id`) USING BTREE,
  CONSTRAINT `course_coursetag_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `course_course` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of course_coursetag
-- ----------------------------
INSERT INTO `course_coursetag` VALUES (9, '1', 114516);
INSERT INTO `course_coursetag` VALUES (1, '114514', 114523);
INSERT INTO `course_coursetag` VALUES (1, '114515', 114524);
INSERT INTO `course_coursetag` VALUES (1, '114516', 114525);

-- ----------------------------
-- Table structure for course_lesson
-- ----------------------------
DROP TABLE IF EXISTS `course_lesson`;
CREATE TABLE `course_lesson`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL,
  `add_time` datetime(6) NULL DEFAULT NULL,
  `course_id` int(0) NOT NULL,
  `video_id` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 114518 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of course_lesson
-- ----------------------------
INSERT INTO `course_lesson` VALUES (114515, '1-112', NULL, 1, 2);
INSERT INTO `course_lesson` VALUES (114516, '222', '2022-07-14 12:53:24.295945', 1, 114514);
INSERT INTO `course_lesson` VALUES (114517, '333', '2022-07-14 13:11:05.441350', 1, 114514);

-- ----------------------------
-- Table structure for video_video
-- ----------------------------
DROP TABLE IF EXISTS `video_video`;
CREATE TABLE `video_video`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL,
  `url` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL,
  `learn_times` int(0) NULL DEFAULT NULL,
  `add_time` datetime(6) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of video_video
-- ----------------------------
INSERT INTO `video_video` VALUES (2, '2', '2', 2, NULL);
INSERT INTO `video_video` VALUES (3, '3', '114515', 5, '2022-07-15 12:28:59.290301');

SET FOREIGN_KEY_CHECKS = 1;
