import React from 'react';

const DashboardPage: React.FC = () => {
    return (
        <div className="p-4">
            <h1 style={{ fontSize: 24, fontWeight: 500 }}>Dashboard</h1>
            <p style={{ color: 'var(--color-text-secondary)' }}>Welcome to FastReport</p>
        </div>
    );
};

export default DashboardPage;
