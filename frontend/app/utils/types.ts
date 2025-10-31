export type SidebarLink = {
  name: string;
  icon: string;
  path: string;
};

export type User = {
  uuid: string;
  /** User's display name */
  displayName: string;
  /** User's username */
  username: string;
  /** User's email address */
  email: string;
  /** User's school */
  school: string;
  /** User's level */
  level: number;
  /** User's experience points */
  xp: number;
};

export type Hackathon = {
  uuid: string;
  /** Name of the hackathon */
  name: string;
  /** Description of the hackathon */
  description: string;
  /** Start date of the hackathon, as a unix timestamp in seconds */
  startDate: number;
  /** End date of the hackathon, as a unix timestamp in seconds */
  endDate: number;
  /** Number of participants in the hackathon */
  participants: number;
};
