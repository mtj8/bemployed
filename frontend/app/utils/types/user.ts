interface User {
  readonly uuid: string;
  /** User's profile gradient colors, as 6-digit hex strings, without the `#` */
  readonly profileGradient: [from: string, to: string];
  /** User's display name */
  displayName: string;
  /** User's username */
  username: string;
  /** User's level */
  level: number;
}

export interface UserProfile extends User {
  /** When the user account was created.
   * @warning Must be parsed from a unix timestamp in seconds
   */
  readonly createdAt: Date;
  /** User's school */
  school: string;
  /** User's graduation year */
  gradYear?: number;
  /** User's email address */
  email: string;
  /** User's experience points */
  xp: number;
  /** Experience points needed to reach the next level */
  xpNeeded: number;
  /** Whether the user's profile is public to other users */
  isPublic: boolean;
  /** User's biography */
  bio: string;
  /** Links to GitHub, LinkedIn, etc. */
  socials: {
    discord: string | null;
    instagram: string | null;
    github: string | null;
    linkedin: string | null;
    personal: string | null;
  };
  /** Array of skill names set by the user */
  skills: string[];
  /** Array of interest names set by the user */
  interests: string[];
}

export interface PublicUser extends User {
  /** If the user is a friend, when the friendship was created.
   * @warning Must be parsed from a unix timestamp in seconds
   */
  readonly friendsSince: Date | null;
  /** Whether the user is blocked by the current user */
  isBlocked: boolean;
}

export type PublicUserProfile = UserProfile & PublicUser;
