from typing import List


class MergeIntervalsRealWorld:
    """Demonstrates real-world applications of merging intervals"""

    def _merge_intervals(self, intervals: List[List[int]]) -> List[List[int]]:
        """Core algorithm: merge overlapping intervals"""
        if not intervals:
            return []

        intervals.sort()
        merged = [intervals[0]]

        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:  # overlap
                merged[-1] = [last[0], max(last[1], current[1])]
            else:  # no overlap
                merged.append(current)

        return merged

    def streaming_video_buffering(self):
        """User pauses/resumes/seeks, find continuously buffered segments"""
        buffered_ranges = [[0, 30], [15, 45], [50, 90], [80, 120]]
        merged = self._merge_intervals(buffered_ranges)

        return {
            "scenario": "Streaming Video Buffering",
            "description": "User pauses, resumes, seeks - find ready-to-play segments",
            "buffered_parts": buffered_ranges,
            "merged": merged,
            "playable": f"Video ready from {merged[0][0]}s-{merged[0][1]}s, then {merged[1][0]}s-{merged[1][1]}s",
            "use_case": "Netflix, YouTube, Twitch"
        }

    def calendar_scheduling(self):
        """Find busy time slots to avoid double-booking"""
        meetings = [[9, 10], [9, 11], [14, 15], [15, 17], [16, 18]]
        merged = self._merge_intervals(meetings)

        return {
            "scenario": "Calendar Meeting Scheduling",
            "description": "Find continuous busy periods to avoid double-booking",
            "meetings": meetings,
            "merged": merged,
            "busy_slots": f"Busy: {merged[0][0]}:00-{merged[0][1]}:00, {merged[1][0]}:00-{merged[1][1]}:00",
            "use_case": "Google Calendar, Outlook, Slack"
        }

    def cpu_memory_usage(self):
        """Track process memory allocation"""
        memory_used = [[100, 200], [150, 300], [500, 700], [600, 750]]
        merged = self._merge_intervals(memory_used)

        return {
            "scenario": "CPU/Memory Usage Tracking",
            "description": "Find continuous memory blocks to optimize allocation",
            "memory_blocks": memory_used,
            "merged": merged,
            "allocation": f"Allocated: {merged[0][0]}-{merged[0][1]}MB, {merged[1][0]}-{merged[1][1]}MB",
            "use_case": "System Monitoring, Docker, Kubernetes"
        }

    def network_packet_loss(self):
        """Determine which packets to resend"""
        lost_packets = [[100, 150], [140, 200], [300, 400], [350, 380]]
        merged = self._merge_intervals(lost_packets)

        return {
            "scenario": "Network Packet Loss Recovery",
            "description": "Group lost packets to resend in batches",
            "lost_ranges": lost_packets,
            "merged": merged,
            "resend": f"Resend packets {merged[0][0]}-{merged[0][1]} and {merged[1][0]}-{merged[1][1]}",
            "use_case": "TCP/IP, CDN, Network Optimization"
        }

    def video_advertising(self):
        """Determine where ads appear in video"""
        ad_slots = [[0, 10], [8, 15], [20, 30], [28, 35]]
        merged = self._merge_intervals(ad_slots)

        return {
            "scenario": "Video Advertising Placement",
            "description": "Merge overlapping ad slots to avoid duplicate ads",
            "ad_ranges": ad_slots,
            "merged": merged,
            "placement": f"Ads shown: {merged[0][0]}-{merged[0][1]}s, {merged[1][0]}-{merged[1][1]}s",
            "use_case": "YouTube, Hulu, Advertising Platforms"
        }

    def dna_sequencing(self):
        """Find continuous gene sequences"""
        gene_regions = [[100, 500], [400, 800], [900, 1200], [950, 1100]]
        merged = self._merge_intervals(gene_regions)

        return {
            "scenario": "DNA/Genome Sequencing",
            "description": "Find continuous gene sequences from overlapping reads",
            "gene_ranges": gene_regions,
            "merged": merged,
            "sequences": f"Gene 1: {merged[0][0]}-{merged[0][1]}, Gene 2: {merged[1][0]}-{merged[1][1]}",
            "use_case": "Bioinformatics, Medical Research, 23andMe"
        }

    def user_availability(self):
        """Find when user is continuously online"""
        online_periods = [[9, 12], [11, 14], [16, 18], [17, 20]]
        merged = self._merge_intervals(online_periods)

        return {
            "scenario": "User Availability Tracking",
            "description": "Find continuous online periods for scheduling",
            "online_times": online_periods,
            "merged": merged,
            "availability": f"Online: {merged[0][0]}:00-{merged[0][1]}:00, {merged[1][0]}:00-{merged[1][1]}:00",
            "use_case": "Slack, Teams, Video Conferencing"
        }

    def flight_seat_availability(self):
        """Find continuous empty seat rows"""
        occupied_seats = [[1, 10], [8, 15], [20, 25], [30, 35], [32, 40]]
        merged = self._merge_intervals(occupied_seats)
        empty_rows = []

        prev_end = 0
        for start, end in merged:
            if start > prev_end:
                empty_rows.append([prev_end, start])
            prev_end = end

        return {
            "scenario": "Flight Seat Availability",
            "description": "Find continuous empty seat rows for group bookings",
            "occupied_rows": occupied_seats,
            "merged_occupied": merged,
            "available_rows": empty_rows if empty_rows else "None",
            "use_case": "Airlines, Ticketing Systems, Kayak"
        }


def main():
    solver = MergeIntervalsRealWorld()
    applications = [
        solver.streaming_video_buffering(),
        solver.calendar_scheduling(),
        solver.cpu_memory_usage(),
        solver.network_packet_loss(),
        solver.video_advertising(),
        solver.dna_sequencing(),
        solver.user_availability(),
        solver.flight_seat_availability(),
    ]

    print("\n" + "="*90)
    print(" MERGE INTERVALS: 8 REAL-WORLD APPLICATIONS ".center(90))
    print("="*90 + "\n")

    for i, app in enumerate(applications, 1):
        print(f"[{i}] {app['scenario'].upper()}")
        print(f"    Description: {app['description']}")
        print(f"    Input: {app.get('buffered_parts') or app.get('meetings') or app.get('memory_blocks') or app.get('lost_ranges') or app.get('ad_ranges') or app.get('gene_ranges') or app.get('online_times') or app.get('occupied_seats')}")
        print(f"    Merged: {app.get('merged') or app.get('merged_occupied')}")
        print(f"    Result: {app[list(app.keys())[-2]]}")  # second-to-last key
        print(f"    Use Case: {app['use_case']}")
        print()

    print("="*90)
    print("Key Insight: Same algorithm solves different domain problems!")
    print("="*90 + "\n")


if __name__ == "__main__":
    main()
