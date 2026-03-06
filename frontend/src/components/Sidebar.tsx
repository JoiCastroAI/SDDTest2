import React, { useState } from 'react';
import { NavLink } from 'react-router-dom';
import { Grid, Building, ChevronLeft, ChevronRight } from 'react-bootstrap-icons';

const Sidebar: React.FC = () => {
    const [collapsed, setCollapsed] = useState(false);

    return (
        <aside className={`sidebar ${collapsed ? 'collapsed' : ''}`}>
            <div className="sidebar-header">
                <div className="sidebar-logo">
                    <div className="sidebar-logo-icon">FR</div>
                    <span className="sidebar-logo-text">FastReport</span>
                </div>
                <button
                    className="sidebar-toggle"
                    onClick={() => setCollapsed(!collapsed)}
                    aria-label={collapsed ? 'Expand sidebar' : 'Collapse sidebar'}
                >
                    {collapsed ? <ChevronRight size={20} /> : <ChevronLeft size={20} />}
                </button>
            </div>
            <nav className="sidebar-nav">
                <NavLink
                    to="/"
                    end
                    className={({ isActive }) => `sidebar-nav-link ${isActive ? 'active' : ''}`}
                >
                    <Grid size={20} />
                    <span className="sidebar-nav-text">Dashboard</span>
                </NavLink>
                <NavLink
                    to="/companies"
                    className={({ isActive }) => `sidebar-nav-link ${isActive ? 'active' : ''}`}
                >
                    <Building size={20} />
                    <span className="sidebar-nav-text">Companies</span>
                </NavLink>
            </nav>
        </aside>
    );
};

export default Sidebar;
