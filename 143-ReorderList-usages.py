class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Singly linked list with an in-place reorder operation:
    L0 -> L1 -> ... -> Ln  becomes  L0 -> Ln -> L1 -> Ln-1 -> L2 -> ...
    """

    def __init__(self, values=None):
        self.head = None
        if values:
            for value in values:
                self.append(value)

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def to_list(self):
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return values

    def reorder(self):
        """Do not return anything, modify head in-place instead."""
        if not self.head or not self.head.next:
            return

        # find middle
        slow, fast = self.head, self.head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the 2nd half
        second = slow.next
        slow.next = None
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge both halves, alternating
        first, second = self.head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


class ReorderListRealWorld:
    """Demonstrates 8 real-world applications of the reorder-list interleave pattern"""

    def _reorder(self, values: list) -> list:
        """Helper: build a LinkedList, reorder it, and return the resulting values"""
        linked_list = LinkedList(values)
        linked_list.reorder()
        return linked_list.to_list()

    def tournament_bracket_seeding(self):
        """Pair strongest seed with weakest seed for round 1 matchups"""
        seeds = [1, 2, 3, 4, 5, 6, 7, 8]  # 1 = strongest
        bracket_order = self._reorder(seeds)

        return {
            "scenario": "Tournament Bracket Seeding",
            "description": "Pairing top seeds against bottom seeds in round 1",
            "seeds_by_rank": seeds,
            "result": f"Matchup order: {bracket_order}",
            "use_case": "Sports Brackets, Esports Tournaments, Chess Pairings"
        }

    def playlist_energy_pacing(self):
        """Alternate low and high energy tracks for better listener pacing"""
        tracks_by_energy = ["track-1(chill)", "track-2(mellow)", "track-3(upbeat)", "track-4(peak)"]
        pacing_order = self._reorder(tracks_by_energy)

        return {
            "scenario": "Playlist Energy Pacing",
            "description": "Interleaving calm and high-energy tracks instead of two similar songs back-to-back",
            "tracks_low_to_high_energy": tracks_by_energy,
            "result": f"Playback order: {pacing_order}",
            "use_case": "Spotify/Apple Music Autoplay, DJ Set Building"
        }

    def print_queue_fairness(self):
        """Alternate large and small print jobs so small jobs don't starve"""
        jobs_by_pages = ["job-A(2pg)", "job-B(5pg)", "job-C(9pg)", "job-D(40pg)"]
        fair_queue = self._reorder(jobs_by_pages)

        return {
            "scenario": "Print/Batch Queue Fairness",
            "description": "Alternating small and large jobs so short jobs aren't stuck behind long ones",
            "jobs_smallest_to_largest": jobs_by_pages,
            "result": f"Serving order: {fair_queue}",
            "use_case": "Print Spoolers, Batch Job Schedulers, Fair Queuing"
        }

    def exam_question_difficulty_ordering(self):
        """Alternate hard and easy questions to manage student pacing/morale"""
        questions_by_difficulty = ["Q1-easy", "Q2-medium", "Q3-hard", "Q4-hardest"]
        exam_order = self._reorder(questions_by_difficulty)

        return {
            "scenario": "Exam Question Ordering",
            "description": "Interleaving hardest and easiest questions instead of a difficulty ramp",
            "questions_easy_to_hard": questions_by_difficulty,
            "result": f"Exam sequence: {exam_order}",
            "use_case": "Adaptive Testing, Online Course Platforms, Quiz Generators"
        }

    def cpu_task_load_balancing(self):
        """Alternate heavy and light tasks on a single worker to smooth out load spikes"""
        tasks_by_duration_ms = ["t1(10ms)", "t2(50ms)", "t3(120ms)", "t4(400ms)"]
        execution_order = self._reorder(tasks_by_duration_ms)

        return {
            "scenario": "CPU/Worker Load Balancing",
            "description": "Alternating short and long tasks to avoid long idle-vs-blocked spikes",
            "tasks_shortest_to_longest": tasks_by_duration_ms,
            "result": f"Execution order: {execution_order}",
            "use_case": "Task Schedulers, Round-Robin Workers, CI Job Runners"
        }

    def presentation_slide_pacing(self):
        """Alternate dense and light slides so a deck doesn't front/back-load content"""
        slides_by_density = ["slide-1(light)", "slide-2(medium)", "slide-3(dense)", "slide-4(densest)"]
        deck_order = self._reorder(slides_by_density)

        return {
            "scenario": "Presentation Slide Pacing",
            "description": "Interleaving dense and light slides to keep audience attention",
            "slides_light_to_dense": slides_by_density,
            "result": f"Deck order: {deck_order}",
            "use_case": "Slide Decks, Onboarding Flows, Investor Pitches"
        }

    def customer_feedback_review_balancing(self):
        """Alternate glowing and critical reviews for a balanced summary report"""
        reviews_by_sentiment = ["review-1(neutral)", "review-2(positive)", "review-3(very positive)", "review-4(negative)"]
        report_order = self._reorder(reviews_by_sentiment)

        return {
            "scenario": "Customer Feedback Report Balancing",
            "description": "Interleaving positive and negative reviews to avoid a lopsided summary",
            "reviews_sorted_by_sentiment": reviews_by_sentiment,
            "result": f"Report order: {report_order}",
            "use_case": "Product Review Digests, Support Ticket Summaries, NPS Reports"
        }

    def survey_question_bias_reduction(self):
        """Alternate most and least salient prompts to counter primacy/recency bias"""
        prompts_by_salience = ["p1(low)", "p2(medium)", "p3(high)", "p4(highest)"]
        survey_order = self._reorder(prompts_by_salience)

        return {
            "scenario": "Survey Question Bias Reduction",
            "description": "Interleaving salient and neutral prompts to reduce serial-position bias in responses",
            "prompts_low_to_high_salience": prompts_by_salience,
            "result": f"Survey order: {survey_order}",
            "use_case": "Market Research, UX Research, Psychology Experiments"
        }


def main():
    solver = ReorderListRealWorld()
    applications = [
        solver.tournament_bracket_seeding(),
        solver.playlist_energy_pacing(),
        solver.print_queue_fairness(),
        solver.exam_question_difficulty_ordering(),
        solver.cpu_task_load_balancing(),
        solver.presentation_slide_pacing(),
        solver.customer_feedback_review_balancing(),
        solver.survey_question_bias_reduction(),
    ]

    print("\n" + "=" * 80)
    print(" REORDER LIST: 8 REAL-WORLD APPLICATIONS ".center(80))
    print("=" * 80 + "\n")

    for i, app in enumerate(applications, 1):
        print(f"[{i}] {app['scenario'].upper()}")
        print(f"    Description: {app['description']}")
        print(f"    Use Case: {app['use_case']}")
        print(f"    Result: {app['result']}")
        print()

    print("=" * 80)
    print("Key Insight: All use the same L0->Ln->L1->Ln-1... interleave to solve different problems!")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
