<script lang="ts">
    import { callFunction } from 'tauri-plugin-python-api';
    let thatbutton: HTMLElement | undefined;
    async function testClick() {
        if (thatbutton) {
            thatbutton.textContent = await callFunction("greet_python", ["from js!!!"]);
        }
    }
</script>

<div class="prose grid place-items-center h-full">
    <div>
        <h1 class="text-xl font-bold">Welcome to EyeTrackVR</h1>
        <div class="py-1"></div> 
        <p>We need to configure some settings before we can continue</p>
        
        <div class="py-4"></div>
        <div class="flex justify-end">
            <a href="/setup" class="btn btn-primary">Let's go!</a>
            <button class="btn btn-secondary" bind:this={thatbutton} on:click={testClick}>Python test</button>
        </div>
    </div>
</div>