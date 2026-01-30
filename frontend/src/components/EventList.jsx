import { useEffect, useState } from "react";
import { fetchEvents } from "../services/api";

const formatEvent = (event) => {
  const time = new Date(event.timestamp).toUTCString();

  switch (event.action) {
    case "PUSH":
      return `${event.author} pushed to ${event.to_branch} on ${time}`;

    case "PULL_REQUEST":
      return `${event.author} submitted a pull request from ${event.from_branch} to ${event.to_branch} on ${time}`;

    case "MERGE":
      return `${event.author} merged branch ${event.from_branch} to ${event.to_branch} on ${time}`;

    default:
      return "";
  }
};

const EventList = () => {
  const [events, setEvents] = useState([]);

  const loadEvents = async () => {
    try {
      const res = await fetchEvents();
      setEvents(res.data);
    } catch (error) {
      console.error("Failed to fetch events", error);
    }
  };

  useEffect(() => {
    loadEvents();

    const interval = setInterval(() => {
      loadEvents();
    }, 15000); // ⏱ poll every 15 seconds

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="events-container">
      {events.map((event) => (
        <div key={event._id} className="event-card">
          {formatEvent(event)}
        </div>
      ))}
    </div>
  );
};

export default EventList;
