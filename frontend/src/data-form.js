import { useState } from 'react';
import {
    Box,
    TextField,
    Button,
} from '@mui/material';
import axios from 'axios';

const endpointMapping = {
    'Notion': 'notion',
    'Airtable': 'airtable',
    'Hubspot': 'hubspot'
};

export const DataForm = ({ integrationType, credentials }) => {
    const [loadedData, setLoadedData] = useState(null);
    const endpoint = endpointMapping[integrationType];

    const handleLoad = async () => {
        try {
            const formData = new FormData();
            formData.append('credentials', JSON.stringify(credentials));
            const response = await axios.post(`http://localhost:8000/integrations/${endpoint}/load`, formData);
            setLoadedData(response.data); // Ensure data is updated here
        } catch (e) {
            alert(e?.response?.data?.detail || 'An error occurred');
        }
    };

    const formatLoadedData = (data) => {
        if (!data) return ''; // Handle empty data gracefully
        if (Array.isArray(data)) {
            return JSON.stringify(data, null, 2); // Prettify array of objects
        } else if (typeof data === 'object') {
            return JSON.stringify(data, null, 2); // Prettify single object
        }
        return data; // Return as is for strings or null values
    };

    return (
        <Box display='flex' justifyContent='center' alignItems='center' flexDirection='column' width='100%'>
            <Box display='flex' flexDirection='column' width='100%'>
                <TextField
                    label="Loaded Data"
                    value={formatLoadedData(loadedData)}
                    sx={{ mt: 2 }}
                    InputLabelProps={{ shrink: true }}
                    multiline
                    minRows={4}
                    disabled
                />
                <Button
                    onClick={handleLoad}
                    sx={{ mt: 2 }}
                    variant='contained'
                >
                    Load Data
                </Button>
                <Button
                    onClick={() => setLoadedData(null)}
                    sx={{ mt: 1 }}
                    variant='contained'
                >
                    Clear Data
                </Button>
            </Box>
        </Box>
    );
};
