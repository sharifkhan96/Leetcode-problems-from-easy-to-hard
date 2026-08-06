from typing import List


class MeetingRoomsII:
    """Find minimum rooms/resources needed - counts maximum overlapping intervals"""

    def min_meeting_rooms(self, intervals: List[List[int]]) -> int:
        """Core algorithm: find max simultaneous meetings at any point"""
        if not intervals:
            return 0

        # Separate start and end times
        times = []
        for start, end in intervals:
            times.append((start, 1))      # 1 for start
            times.append((end, -1))       # -1 for end

        times.sort()

        max_rooms = 0
        current_rooms = 0

        for _, event_type in times:
            current_rooms += event_type
            max_rooms = max(max_rooms, current_rooms)

        return max_rooms


class MeetingRoomsIIRealWorld(MeetingRoomsII):
    """Real-world applications of meeting room scheduling"""

    def conference_room_booking(self):
        """Corporate office conference room scheduling"""
        meetings = [[9, 10], [9, 11], [11, 12], [10, 11]]
        rooms_needed = self.min_meeting_rooms(meetings)

        return {
            "scenario": "Conference Room Booking",
            "description": "Find minimum conference rooms needed",
            "meetings": meetings,
            "result": f"{rooms_needed} conference rooms required",
            "details": "At 10:00 AM, meetings [9,10], [9,11], [10,11] overlap → need 3 rooms",
            "use_case": "Google Meet, Outlook, Slack, Corporate offices"
        }

    def classroom_scheduling(self):
        """University classroom allocation"""
        classes = [[8, 9], [8, 10], [9, 10], [10, 11], [9, 11]]
        rooms_needed = self.min_meeting_rooms(classes)

        return {
            "scenario": "Classroom Scheduling",
            "description": "Minimum classrooms needed in a university",
            "class_times": classes,
            "result": f"{rooms_needed} classrooms required",
            "details": "Peak overlap at 9:00-10:00 AM with 4 simultaneous classes",
            "use_case": "University Course Management, School Timetables"
        }

    def hospital_operating_rooms(self):
        """Hospital surgery scheduling"""
        surgeries = [[7, 8], [7, 9], [8, 10], [9, 10], [8, 11]]
        rooms_needed = self.min_meeting_rooms(surgeries)

        return {
            "scenario": "Hospital Operating Rooms",
            "description": "Minimum OR (Operating Rooms) needed for surgeries",
            "surgery_times": surgeries,
            "result": f"{rooms_needed} operating rooms required",
            "details": "Peak: 8:00-10:00 AM needs 3 simultaneous ORs for surgeries",
            "use_case": "Hospital Management, Healthcare Scheduling, Surgery Booking"
        }

    def parking_lot_capacity(self):
        """Parking lot occupancy management"""
        parking_sessions = [[8, 10], [9, 11], [9, 12], [10, 13], [11, 14]]
        spots_needed = self.min_meeting_rooms(parking_sessions)

        return {
            "scenario": "Parking Lot Capacity",
            "description": "Minimum parking spots needed at peak time",
            "car_occupancy": parking_sessions,
            "result": f"{spots_needed} parking spots required",
            "details": "Peak occupancy 10:00-11:00 AM: 4 cars parked simultaneously",
            "use_case": "Parking Management, Mall/Airport Parking, Valet Services"
        }

    def server_resource_allocation(self):
        """Cloud server load balancing"""
        job_durations = [[100, 150], [120, 200], [150, 180], [160, 220]]
        servers_needed = self.min_meeting_rooms(job_durations)

        return {
            "scenario": "Server Resource Allocation",
            "description": "Minimum servers needed for concurrent jobs",
            "job_times": job_durations,
            "result": f"{servers_needed} servers required",
            "details": "Peak concurrency at time 150-160: 3 jobs running simultaneously",
            "use_case": "AWS, Google Cloud, Kubernetes, Load Balancing"
        }

    def restaurant_table_management(self):
        """Restaurant table reservation and turnover"""
        reservations = [[18, 19], [18, 20], [19, 20], [19, 21], [20, 21]]
        tables_needed = self.min_meeting_rooms(reservations)

        return {
            "scenario": "Restaurant Table Management",
            "description": "Minimum tables needed during peak dining hours",
            "reservation_times": reservations,
            "result": f"{tables_needed} tables required",
            "details": "7:00-8:00 PM peak: 4 tables occupied simultaneously",
            "use_case": "OpenTable, Resy, Restaurant Booking Systems"
        }

    def movie_theater_scheduling(self):
        """Movie theater screen allocation"""
        showtimes = [[14, 16], [14, 17], [15, 17], [16, 18], [16, 19]]
        screens_needed = self.min_meeting_rooms(showtimes)

        return {
            "scenario": "Movie Theater Screen Scheduling",
            "description": "Minimum screens needed for concurrent showings",
            "showtime_windows": showtimes,
            "result": f"{screens_needed} screens required",
            "details": "3:00-4:00 PM: 4 movies showing simultaneously",
            "use_case": "Cinema Ticketing, Fandango, AMC Theaters"
        }

    def customer_service_queue(self):
        """Call center or support queue management"""
        call_durations = [[8, 9], [8, 10], [8, 11], [9, 10], [9, 12]]
        agents_needed = self.min_meeting_rooms(call_durations)

        return {
            "scenario": "Customer Service Queue",
            "description": "Minimum support agents needed for call volume",
            "call_times": call_durations,
            "result": f"{agents_needed} support agents required",
            "details": "9:00-10:00 AM: 4 calls active → need 4 agents",
            "use_case": "Call Centers, Customer Support, Help Desks"
        }

    def atm_cash_withdrawal_lanes(self):
        """ATM or toll booth lane capacity"""
        withdrawal_times = [[10, 11], [10, 12], [10, 13], [11, 12], [11, 13]]
        lanes_needed = self.min_meeting_rooms(withdrawal_times)

        return {
            "scenario": "ATM/Toll Booth Lanes",
            "description": "Minimum lanes needed for peak traffic",
            "transaction_times": withdrawal_times,
            "result": f"{lanes_needed} lanes required",
            "details": "Peak 11:00 AM: 3 transactions in progress",
            "use_case": "Bank ATM Networks, Toll Booths, Highway Capacity Planning"
        }

    def gym_class_capacity(self):
        """Fitness gym class room capacity"""
        class_intervals = [[6, 7], [6, 7.5], [7, 8], [7.5, 8.5], [8, 9]]
        # Convert to minutes: 6:00=360, 7:30=450, etc.
        intervals_minutes = [[int(start*60), int(end*60)] for start, end in class_intervals]
        rooms_needed = self.min_meeting_rooms(intervals_minutes)

        return {
            "scenario": "Gym Class Capacity",
            "description": "Minimum studios needed for concurrent fitness classes",
            "class_times": ["6:00-7:00", "6:30-7:30", "7:00-8:00", "7:30-8:30", "8:00-9:00"],
            "result": f"{rooms_needed} studios required",
            "details": "Peak 7:00-7:30 AM: 3 classes overlapping",
            "use_case": "Peloton, ClassPass, Gym Management Software"
        }


def main():
    solver = MeetingRoomsIIRealWorld()
    applications = [
        solver.conference_room_booking(),
        solver.classroom_scheduling(),
        solver.hospital_operating_rooms(),
        solver.parking_lot_capacity(),
        solver.server_resource_allocation(),
        solver.restaurant_table_management(),
        solver.movie_theater_scheduling(),
        solver.customer_service_queue(),
        solver.atm_cash_withdrawal_lanes(),
        solver.gym_class_capacity(),
    ]

    print("\n" + "="*95)
    print(" MEETING ROOMS II: 10 REAL-WORLD APPLICATIONS ".center(95))
    print("="*95 + "\n")

    for i, app in enumerate(applications, 1):
        print(f"[{i}] {app['scenario'].upper()}")
        print(f"    Description: {app['description']}")

        # Find and print input
        input_keys = [k for k in app.keys() if any(x in k for x in ['meetings', 'times', 'occupancy', 'durations', 'windows'])]
        if input_keys:
            print(f"    Input: {app[input_keys[0]]}")

        print(f"    Result: {app['result']}")
        print(f"    Details: {app['details']}")
        print(f"    Use Case: {app['use_case']}")
        print()

    print("="*95)
    print("Key Insight: Count max overlaps to find minimum resources needed!")
    print("="*95 + "\n")


if __name__ == "__main__":
    main()
