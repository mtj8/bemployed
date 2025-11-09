export interface SidebarLink {
  readonly name: string;
  readonly icon: string;
  readonly path: string;
  readonly customActiveTest?: () => boolean;
}

export interface Team {
  readonly uuid: string;
  name: string;
  /** When the team was created.
   * @warning Must be parsed from a unix timestamp in seconds
   */
  readonly createdAt: Date;
  readonly members: PublicUser[];
}

export interface Hackathon {
  readonly uuid: string;
  /** Name of the hackathon */
  name: string;
  /** Description of the hackathon */
  description: string;
  /** Start date of the hackathon.
   * @warning Must be parsed from a unix timestamp in seconds
   */
  startDate: Date;
  /** End date of the hackathon.
   * @warning Must be parsed from a unix timestamp in seconds
   */
  endDate: Date;
  /** Number of participants in the hackathon */
  participants: number;
  /** Team of the user in the hackathon, if any */
  team?: Team;
}

export * from "./types/user";
